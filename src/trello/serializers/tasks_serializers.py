from rest_framework import serializers
from trello.models import *
from .subtask_serializers import *
from .comments_serializers import *
from .attachments_serializers import *
from .column_serializers import *
from .column_tasks_serializer import ColumnTasksDetailSerializer


class TaskDetailSerializer(serializers.ModelSerializer):
    subtasks = SubtaskDetailSerializer(read_only=True, many=True)
    comments = CommentDetailSerializer(read_only=True, many=True)
    attachments = AttachmentDetailSerializer(read_only=True, many=True)

    class Meta:
        model = Task
        fields = (
        'owner', 'column', 'assignee', 'title', 'attachments', 'is_complete', 'description', 'subtasks', 'comments')


class TasksAssigneeListSerializer(serializers.ModelSerializer):
    column = ColumnTasksDetailSerializer(read_only=True, many=False)

    class Meta:
        model = Task
        fields = ('column', 'assignee', 'title', 'due_date', 'created_at', 'is_complete', 'description',)
