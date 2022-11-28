from rest_framework.routers import DefaultRouter
from log.views import LogViewSet


router = DefaultRouter()

router.register(
    r'projects/(?P<project_id>\d+)/logs', LogViewSet, basename='logs'
)

urlpatterns = router.urls
