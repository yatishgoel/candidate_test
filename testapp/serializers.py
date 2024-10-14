from rest_framework import serializers
from .models import CandidateTimestamp
from collections import defaultdict
from django.utils import timezone

class CandidateTimestampSerializer(serializers.ModelSerializer):
    class Meta:
        model = CandidateTimestamp
        fields = ['id', 'timestamp', 'value', 'year', 'month', 'day', 'created_at', 'updated_at']
        read_only_fields = ['year', 'month', 'day', 'created_at', 'updated_at']

    def to_representation(self, instance):
        return {
            'id': instance.id,
            'timestamp': instance.timestamp.strftime('%Y/%m/%d , %H:%M:%S'),
            'value': instance.value,
            'year': instance.year,
            'month': instance.month,
            'day': instance.day,
            'created_at': instance.created_at.isoformat(),
            'updated_at': instance.updated_at.isoformat()
        }

    def validate_timestamp(self, value):
        if value > timezone.now():
            raise serializers.ValidationError("Timestamp cannot be in the future.")
        return value

    def create(self, validated_data):
        return CandidateTimestamp.objects.create(**validated_data)

    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance

class StructuredCandidateTimestampSerializer(serializers.Serializer):
    @staticmethod
    def get_structured_data(data):
        structured_data = defaultdict(lambda: defaultdict(list))

        # Ensure data is always a list
        if not isinstance(data, (list, tuple)):
            data = [data]

        for item in data:
            year = item.timestamp.year
            month = item.timestamp.month
            timestamp = item.timestamp.strftime('%Y/%m/%d , %H:%M:%S')
            value = item.value

            structured_data[year][month].append({timestamp: value})

        return [
            {year: [{month: month_data} for month, month_data in sorted(year_data.items())]}
            for year, year_data in sorted(structured_data.items())
        ]

    def to_representation(self, instance):
        return self.get_structured_data(instance)[0]