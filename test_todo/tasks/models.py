from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Task(models.Model):
    """
    Модель задачи
    """
    STATUS_CHOICES = (
        ('P', 'Pending'),
        ('I', 'In Progress'),
        ('C', 'Completed')
    )
    title = models.CharField(
        verbose_name="Название задачи",
        max_length=150,
        help_text="Введите название задачи",
    )
    description = models.TextField(
        verbose_name="Описание задачи",
        help_text="Опишите задачу",
        blank=True,
    )
    status = models.CharField(
        verbose_name="Статус",
        max_length=15,
        db_index=True,
        choices=STATUS_CHOICES,
    )
    due_date = models.DateTimeField(
        verbose_name="Срок выполнения задачи",
        blank=True,
        null=True,
        db_index=True,
    )
    created_at = models.DateTimeField(
        verbose_name="Дата создания задачи",
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        verbose_name="Дата последнего обновления",
        auto_now=True
    )
    user = models.ForeignKey(
        User,
        verbose_name="Автор задачи",
        on_delete=models.CASCADE,
    )


class Comment(models.Model):
    """
    Модель комментария
    """
    text = models.TextField(verbose_name="Текст коммертария")
    created_at = models.DateTimeField(
        verbose_name="Дата создания комментария",
        auto_now_add=True,
        db_index=True
    )
    task = models.ForeignKey(
        Task,
        verbose_name="Комментируемая задача",
        on_delete=models.CASCADE,
        related_name='comments'
    )
    user = models.ForeignKey(
        User,
        verbose_name="Автор комментария",
        on_delete=models.CASCADE,
        related_name='comments'
    )
