from django.shortcuts import get_object_or_404
from rest_framework import viewsets

from project.models import Project
from .models import Log
from .permissions import LogPermission
from .serializers import LogSerializer


class LogViewSet(viewsets.ModelViewSet):
    serializer_class = LogSerializer
    permission_classes = (LogPermission,)

    def get_queryset(self):
        return Log.objects.select_related('project').filter(
            project__id=self.kwargs['project_id']
        )

    def perform_create(self, serializer):
        current_project_id = self.kwargs['project_id']
        current_project = get_object_or_404(Project, id=current_project_id)
        serializer.save(project=current_project, creator=self.request.user)
