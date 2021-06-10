from rest_framework import serializers
from trello.models import *
from .column_serializers import *


class ProjectDetailSerializer(serializers.ModelSerializer):
	columns = ColumnDetailSerializer(read_only=True, many=True)

	class Meta:
		model = Project
		fields = ('owner', 'managers', 'name', 'discord_url', 'columns')


class ProjectListSerializer(serializers.ModelSerializer):
	class Meta:
		model = Project
		fields = '__all__'
