from rest_framework import generics
from rest_framework.generics import get_object_or_404
from trello.permissions import *
from trello.models import *
from rest_framework.permissions import IsAuthenticated
from trello.serializers.project_serializers import *


class ProjectDetailView(generics.RetrieveUpdateDestroyAPIView):
	serializer_class = ProjectDetailSerializer
	queryset = Project.objects.all()
	permission_classes = (IsAuthenticated, IsOwnerOrManagerForProject)


class ProjectCreateView(generics.CreateAPIView):
	serializer_class = ProjectDetailSerializer
	permission_classes = (IsAuthenticated, IsOwnerOrManagerForProject)

	def perform_create(self, serializer):
		serializer.save(owner=self.request.user)


class ProjectListSerializer(generics.ListAPIView):
	serializer_class = ProjectListSerializer
	queryset = Project.objects.all()
	permission_classes = (IsAuthenticated, IsOwnerOrManagerForProject)

	def get_queryset(self):
		user = self.request.user
		return Project.objects.filter(owner=user)


class ProjectAddManagerView(generics.CreateAPIView):
	serializer_class = ProjectDetailSerializer
	queryset = Project.objects.all()
	permissions = (IsAuthenticated, IsOwnerOrManagerForProject)

	def get_queryset(self):
		project = self.request.data.project
		return Project.objects.filter(id=project)
