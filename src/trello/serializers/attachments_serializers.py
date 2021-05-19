from rest_framework import serializers
from trello.models import *


class AttachmentDetailSerializer(serializers.ModelSerializer):
	class Meta:
		model = Attachment
		fields = '__all__'
