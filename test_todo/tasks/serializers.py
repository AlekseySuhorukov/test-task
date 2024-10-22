import pytz
from datetime import datetime
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from tasks.models import Comment, Task


class TaskSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(slug_field='username',
                                        read_only=True)

    class Meta:
        model = Task
        fields = '__all__'

    def validate_due_date(self, value):
        if value:
            utc = pytz.UTC
            if value < utc.localize(datetime.now()):
                raise ValidationError(
                    {"due_date":
                     "Срок выполнения не должен быть в прошлом"}
                )
        return value


class CommentSerializer(serializers.ModelSerializer):
    task = serializers.PrimaryKeyRelatedField(read_only=True)
    user = serializers.SlugRelatedField(slug_field='username',
                                        read_only=True)

    class Meta:
        fields = '__all__'
        model = Comment
