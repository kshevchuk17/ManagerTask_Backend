from rest_framework import serializers
from .models import *


class UserDetailSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = '__all__'


class ColumnDetailSerializer(serializers.ModelSerializer):
	class Meta:
		model = Column
		fields = '__all__'


class TaskDetailSerializer(serializers.ModelSerializer):
	class Meta:
		model = Task
		fields = '__all__'


class SubtaskDetailSerializer(serializers.ModelSerializer):
	class Meta:
		model = Subtask
		fields = '__all__'


class CommentDetailSerializer(serializers.ModelSerializer):
	class Meta:
		model = Comment
		fields = '__all__'


class ProjectDetailSerializer(serializers.ModelSerializer):
	column = ColumnDetailSerializer(read_only=True, many=True)
	task = TaskDetailSerializer(read_only=True, many=True)
	subtask = SubtaskDetailSerializer(read_only=True, many=True)
	comment = ColumnDetailSerializer(read_only=True, many=True)

	class Meta:
		model = Project
		fields = ('user', 'name', 'column', 'task', 'subtask', 'comment')
