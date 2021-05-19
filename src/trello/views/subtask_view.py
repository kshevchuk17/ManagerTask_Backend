from django.shortcuts import render
from rest_framework import generics
from rest_framework.generics import get_object_or_404
from trello.permissions import *
from trello.models import *
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from trello.serializers.subtask_serializers import *


class SubtaskCreateView(generics.CreateAPIView):
	serializer_class = SubtaskDetailSerializer
	permission_classes = (IsAuthenticated,)

	def perform_create(self, serializer):
		task = Task.objects.get(id=self.request.data.get('task'))
		print('=================================')
		print(task)
		serializer.save(task=task)


class SubtaskDetailView(generics.RetrieveUpdateDestroyAPIView):
	serializer_class = SubtaskDetailSerializer
	queryset = Subtask.objects.all()
	permission_classes = (IsAuthenticated, IsOwnerReadOnly, IsAdminUser)

