import logging
from collections import defaultdict
from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import CandidateTimestamp
from .serializers import CandidateTimestampSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from rest_framework.pagination import PageNumberPagination
from django.core.cache import cache
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

logger = logging.getLogger(__name__)
CACHE_TIMEOUT = 60*60*24 # 1 day

class StandardResultsSetPagination(PageNumberPagination):
    page_size = 100
    page_size_query_param = 'page_size'
    max_page_size = 1000

class CandidateTimestampViewSet(viewsets.ModelViewSet):
    queryset = CandidateTimestamp.objects.all()
    serializer_class = CandidateTimestampSerializer
    pagination_class = StandardResultsSetPagination
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ['year', 'month', 'day', 'timestamp', 'value']
    ordering_fields = ['year', 'month', 'day', 'timestamp', 'value']

    def restructure_data(self, nested_data):
        structured_data = defaultdict(lambda: defaultdict(list))
        for item in nested_data:
            structured_data[item.year][item.month].append({
                item.timestamp.strftime('%H:%M:%S'): item.value
            })
        result = []
        for item in structured_data:
            result.append({item: [{i: structured_data[item][i]} for i in structured_data[item]]})
        return result

    def create(self, request, *args, **kwargs):
        data = request.data
        many = isinstance(data, list)
        serializer = self.get_serializer(data=data, many=many)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        serializer.save()

    def get_cache_key(self, request):
        query_params = request.query_params.copy()
        query_params.pop('page', None)  # Remove page from cache key
        sorted_params = sorted(query_params.items())
        return f'candidate_timestamp_list:{",".join([f"{k}={v}" for k, v in sorted_params])}'

    def list(self, request, *args, **kwargs):
        cache_key = self.get_cache_key(request)
        cached_data = cache.get(cache_key)

        if cached_data is not None:
            return Response(cached_data)

        try:
            queryset = self.filter_queryset(self.get_queryset())
            page = self.paginate_queryset(queryset)
            
            if page is not None:
                structured_data = self.restructure_data(list(page))
                response_data = self.get_paginated_response(structured_data).data
                response_data['results'] = structured_data
                cache.set(cache_key, response_data, timeout=CACHE_TIMEOUT)
                return Response(response_data)
            else:
                structured_data = self.restructure_data(list(queryset))
                cache.set(cache_key, structured_data, timeout=CACHE_TIMEOUT)
                return Response(structured_data)
        except Exception as e:
            logger.error(f"Error in list view: {str(e)}")
            return Response({"error": "An unexpected error occurred"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def perform_destroy(self, instance):
        super().perform_destroy(instance)
        invalidate_cache()

def invalidate_cache():
    try:
        cache.clear()
        logger.info("Cache cleared due to CandidateTimestamp data change")
    except Exception as e:
        logger.error(f"Error clearing cache: {str(e)}")
        
@receiver(post_save, sender=CandidateTimestamp)
@receiver(post_delete, sender=CandidateTimestamp)
def handle_data_change(sender, instance, **kwargs):
    invalidate_cache()