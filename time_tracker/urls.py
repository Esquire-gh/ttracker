from django.contrib import admin
from rest_framework.schemas import get_schema_view
from rest_framework.documentation import include_docs_urls
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('project.urls')),

    path('api/users/', include('users.urls')),
    path('docs/', include_docs_urls(title='TimeTracker API')),
    path('schema', get_schema_view(
            title="TimeTracker API",
            description="Project Log Tracker API",
            version="1.0.0"
        ), name='openapi-schema'),
]
