
from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from drf_spectacular.utils import extend_schema
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination

from tasks.models import Comment, Task
from tasks.permissions import IsOwnerOrReadOnly
from tasks.serializers import CommentSerializer, TaskSerializer


@extend_schema(tags=["Tasks"])
class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsOwnerOrReadOnly]
    filter_backends = (DjangoFilterBackend,)
    pagination_class = PageNumberPagination
    filterset_fields = ('status', 'due_date')

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


@extend_schema(tags=["Comments"])
class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsOwnerOrReadOnly]
    pagination_class = PageNumberPagination

    def get_queryset(self):
        task = get_object_or_404(Task, id=self.kwargs['task_id'])
        return task.comments.all()

    def perform_create(self, serializer):
        task = get_object_or_404(Task, id=self.kwargs['task_id'])
        serializer.save(user=self.request.user, task=task)
