from django.urls import include, path
from rest_framework.routers import DefaultRouter

from tasks.views import CommentViewSet, TaskViewSet

router = DefaultRouter()

router.register("tasks", TaskViewSet, "tasks")
router.register(
    r'tasks/(?P<task_id>\d+)/comments',
    CommentViewSet,
    basename='comments'
)

urlpatterns = [
    path("", include(router.urls)),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
]
