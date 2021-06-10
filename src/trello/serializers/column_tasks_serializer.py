from rest_framework import serializers
from trello.models import *
from .projects_column_serializer import ProjectColumnDetailSerializer


class ColumnTasksDetailSerializer(serializers.ModelSerializer):
    project = ProjectColumnDetailSerializer(read_only=True, many=False)

    class Meta:
        model = Column
        fields = ('project', 'name')
