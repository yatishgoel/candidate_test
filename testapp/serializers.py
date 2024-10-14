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