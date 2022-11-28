from django.shortcuts import get_object_or_404
from rest_framework.permissions import BasePermission, SAFE_METHODS

from project.models import Project


class LogPermission(BasePermission):

    def has_permission(self, request, view):
        id = view.kwargs['project_id']
        current_project = get_object_or_404(Project, id=id)

        return request.user in current_project.participants.all() or request.user == current_project.project_owner

    def has_object_permission(self, request, obj):
        if request.method in SAFE_METHODS:
            return True

        return obj.creator == request.user
