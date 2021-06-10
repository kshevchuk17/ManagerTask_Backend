from rest_framework import serializers
from trello.models import *


class ProjectColumnDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('id', 'name')
