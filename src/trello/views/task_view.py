from django.shortcuts import render
from rest_framework import generics
from rest_framework.generics import get_object_or_404
from trello.permissions import *
from trello.models import *
from rest_framework.permissions import IsAuthenticated
from trello.serializers.tasks_serializers import *
from trello.serializers.project_serializers import *


class TaskCreateView(generics.CreateAPIView):
	serializer_class = TaskDetailSerializer
	permission_classes = (IsAuthenticated, IsOwnerOrManagerForTask)

	def perform_create(self, serializer):
		serializer.save(owner=self.request.user)


class TaskDetailView(generics.RetrieveUpdateDestroyAPIView):
	serializer_class = TaskDetailSerializer
	queryset = Task.objects.all()
	permission_classes = (IsAuthenticated, IsOwnerOrManagerForTask)


class TasksAssigneeListView(generics.ListAPIView):
	serializer_class = TasksAssigneeListSerializer
	queryset = Task.objects.all()
	permission_classes = (IsAuthenticated, IsOwnerOrManagerForProject)

	def get_queryset(self):
		user = self.request.user
		return Task.objects.filter(assignee=user)
