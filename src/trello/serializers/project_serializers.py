from rest_framework import serializers
from trello.models import *
from .column_serializers import *


class ProjectDetailSerializer(serializers.ModelSerializer):
	columns = ColumnDetailSerializer(read_only=True, many=True)

	class Meta:
		model = Project
		fields = ('user', 'manager', 'name', 'columns')


class ProjectListSerializer(serializers.ModelSerializer):
	class Meta:
		model = Project
		fields = '__all__'
