from rest_framework import serializers
from trello.models import *


class SubtaskDetailSerializer(serializers.ModelSerializer):
	class Meta:
		model = Subtask
		fields = '__all__'
