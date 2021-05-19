from rest_framework import serializers
from trello.models import *


class CommentDetailSerializer(serializers.ModelSerializer):
	class Meta:
		model = Comment
		fields = '__all__'
