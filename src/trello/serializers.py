from rest_framework import serializers
from .models import *


class UserDetailSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = '__all__'


class SubtaskDetailSerializer(serializers.ModelSerializer):
	class Meta:
		model = Subtask
		fields = '__all__'


class CommentDetailSerializer(serializers.ModelSerializer):
	class Meta:
		model = Comment
		fields = '__all__'


class TaskDetailSerializer(serializers.ModelSerializer):
	subtasks = SubtaskDetailSerializer(read_only=True, many=True)
	comments = CommentDetailSerializer(read_only=True, many=True)

	class Meta:
		model = Task
		fields = ('owner', 'title', 'due_date', 'attachments', 'description', 'subtasks', 'comments')


class ColumnDetailSerializer(serializers.ModelSerializer):
	tasks = TaskDetailSerializer(read_only=True, many=True)

	class Meta:
		model = Column
		fields = ('name', 'tasks')


class ProjectDetailSerializer(serializers.ModelSerializer):
	columns = ColumnDetailSerializer(read_only=True, many=True)

	class Meta:
		model = Project
		fields = ('user', 'name', 'columns')

# =====================================================================================================================


class ProjectListSerializer(serializers.ModelSerializer):
	class Meta:
		model = Project
		fields = '__all__'
