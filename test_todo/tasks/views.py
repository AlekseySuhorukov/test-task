
from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from drf_spectacular.utils import extend_schema, extend_schema_view
from drf_standardized_errors.openapi import AutoSchema
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination

from tasks.models import Comment, Task
from tasks.permissions import IsOwnerOrReadOnly
from tasks.serializers import CommentSerializer, TaskSerializer


@extend_schema(tags=["Tasks"])
@extend_schema_view(
    retrieve=extend_schema(
        summary="Получить конкретную задачу",
    ),
    list=extend_schema(
        summary="Получить список задач",
    ),
    update=extend_schema(
        summary="Полностью измененить существующую задачу",
    ),
    partial_update=extend_schema(
        summary="Частично измененить существующую задачу",
    ),
    create=extend_schema(
        summary="Создать задачу",
    ),
    destroy=extend_schema(
        summary="Удалить задачу",
    ),
)
class TaskViewSet(viewsets.ModelViewSet):
    schema = AutoSchema()
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsOwnerOrReadOnly]
    filter_backends = (DjangoFilterBackend,)
    pagination_class = PageNumberPagination
    filterset_fields = ('status', 'due_date')

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


@extend_schema(tags=["Comments"])
@extend_schema_view(
    retrieve=extend_schema(
        summary="Получить конкретный комментарий",
    ),
    list=extend_schema(
        summary="Получить список комментариев к задаче",
    ),
    update=extend_schema(
        summary="Полностью измененить существующий комментарий",
    ),
    partial_update=extend_schema(
        summary="Частично измененить существующий комментарий",
    ),
    create=extend_schema(
        summary="Создать комментарий",
    ),
    destroy=extend_schema(
        summary="Удалить комментарий",
    ),
)
class CommentViewSet(viewsets.ModelViewSet):
    schema = AutoSchema()
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
