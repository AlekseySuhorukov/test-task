from django.contrib.admin import ModelAdmin, register

from tasks.models import (Comment, Task)


@register(Task)
class IngredientAdmin(ModelAdmin):

    list_display = ("title", "description", "status", "due_date", "user",)
    list_filter = ("title",)
    search_fields = ("title",)


@register(Comment)
class FavoriteAdmin(ModelAdmin):

    list_display = ("text", "task", "user",)
    list_filter = ("user",)
    search_fields = ("user",)
