from rest_framework import serializers
from trello.models import *


class UserDetailSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = '__all__'
