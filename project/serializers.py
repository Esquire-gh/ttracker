from rest_framework import serializers

from project.models import Project
from users.serializers import UserSerializer


class ProjectSerializer(serializers.ModelSerializer):
    project_owner = serializers.CharField(source="project_owner.email", read_only=True)

    class Meta:
        model = Project
        fields = (
            'id',
            'title',
            'description',
            'project_owner',
            'participants',
            'start_date',
            'end_date',
            'duration',
            'created',
            'modified',
        )
        read_only_fields = (
            'id',
            'project_owner',
            'duration',
            'created',
            'modified',
        )

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep["participants"] = UserSerializer(instance.participants.all(), many=True).data
        return rep
