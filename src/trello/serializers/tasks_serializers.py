from rest_framework import serializers
from trello.models import *
from .subtask_serializers import *
from .comments_serializers import *
from .attachments_serializers import *


class TaskDetailSerializer(serializers.ModelSerializer):
	subtasks = SubtaskDetailSerializer(read_only=True, many=True)
	comments = CommentDetailSerializer(read_only=True, many=True)
	attachments = AttachmentDetailSerializer(read_only=True, many=True)

	class Meta:
		model = Task
		fields = ('owner', 'column', 'assignee', 'title', 'attachments', 'description', 'subtasks', 'comments')
