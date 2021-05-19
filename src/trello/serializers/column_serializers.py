from rest_framework import serializers
from trello.models import *
from .tasks_serializers import *


class ColumnDetailSerializer(serializers.ModelSerializer):
	tasks = TaskDetailSerializer(read_only=True, many=True)

	class Meta:
		model = Column
		fields = ('project', 'name', 'tasks')
