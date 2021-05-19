from django.shortcuts import render
from rest_framework import generics
from rest_framework.generics import get_object_or_404
from trello.permissions import *
from trello.models import *
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from trello.serializers.tasks_serializers import *


class TaskCreateView(generics.CreateAPIView):
	serializer_class = TaskDetailSerializer
	permission_classes = (IsAuthenticated, )

	def perform_create(self, serializer):
		column = Column.objects.get(id=self.request.data.get('column'))
		serializer.save(owner=self.request.user)
		serializer.save(column=column)


class TaskDetailView(generics.RetrieveUpdateDestroyAPIView):
	serializer_class = TaskDetailSerializer
	queryset = Task.objects.all()
	permission_classes = (IsAuthenticated, IsOwnerReadOnly, IsAdminUser)
