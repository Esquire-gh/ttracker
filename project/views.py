from rest_framework import viewsets

from project.models import Project
from project.permissions import ProjectOwnerPermission
from project.serializers import ProjectSerializer


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.prefetch_related('participants')
    permission_classes = (ProjectOwnerPermission,)
    serializer_class = ProjectSerializer

    def perform_create(self, serializer):
        serializer.save(project_owner=self.request.user)
