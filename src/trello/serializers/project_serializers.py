from rest_framework import serializers
from trello.models import *
from .column_serializers import *


class ProjectDetailSerializer(serializers.ModelSerializer):
	columns = ColumnDetailSerializer(read_only=True, many=True)

	class Meta:
		model = Project
		fields = ('id', 'owner', 'managers', 'name', 'columns')

	def update(self, instance, validated_data):
		managers = validated_data.pop('managers')
		instance = super(ProjectDetailSerializer, self).update(instance, validated_data)
		admins = instance.managers.all()
		for manager in managers:
			admin = User.objects.get(username=manager)
			if admin in admins:
				instance.managers.remove(admin)
			else:
				instance.managers.add(admin)
		return instance


class ProjectListSerializer(serializers.ModelSerializer):
	class Meta:
		model = Project
		fields = '__all__'
