from django.utils import timezone
from rest_framework import serializers

from log.models import Log


class LogSerializer(serializers.ModelSerializer):

    class Meta:
        model = Log
        fields = (
            'id',
            'project',
            'creator',
            'description',
            'time_started',
            'time_ended',
            'time_spent_in_hours',
        )
        read_only_fields = (
            'id',
            'project',
            'creator',
            'time_spent_in_hours',
        )

    def validate_time_started(self, value):
        if value > timezone.now():
            raise serializers.ValidationError("Cannot create logs in the future.")
        return value

    def validate(self, attrs):
        if attrs['time_started'] > attrs['time_ended']:
            raise serializers.ValidationError(
                {'time_ended': "Log start date cannot exceed end date. "}
            )

        return attrs
