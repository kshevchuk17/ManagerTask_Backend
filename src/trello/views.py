from django.shortcuts import render
from rest_framework import generics
from rest_framework.generics import get_object_or_404
from .serializers import *
# from .permissions import *
from rest_framework.permissions import IsAuthenticated, IsAdminUser


class ProjectDetailView(generics.RetrieveUpdateDestroyAPIView):
	serializer_class = ProjectDetailSerializer
	queryset = Project.objects.all()
	# permission_classes = (IsAuthenticated, )

	def get_object(self):
		obj = get_object_or_404(self.queryset, user=self.request.user)
		return obj


class ProjectCreateView(generics.CreateAPIView):
	serializer_class = ProjectDetailSerializer
	# permission_classes = (IsAuthenticated, )

	def perform_create(self, serializer):
		serializer.save(user=self.request.user)


class ProjectListSerializer(generics.ListAPIView):
	serializer_class = ProjectDetailSerializer
	queryset = Project.objects.all()
	# permission_classes = (IsAuthenticated, )

	def get_queryset(self):
		user = self.request.user
		return Project.objects.filter(user=user)