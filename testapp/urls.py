from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CandidateTimestampViewSet


router = DefaultRouter()
router.register(r'fronted', CandidateTimestampViewSet, basename="fronted")


urlpatterns = [
    path('', include(router.urls)),
]

