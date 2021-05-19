from django.shortcuts import render
from rest_framework import generics
from rest_framework.generics import get_object_or_404
from trello.permissions import *
from trello.models import *
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from trello.serializers.column_serializers import *


class ColumnCreateView(generics.CreateAPIView):
	serializer_class = ColumnDetailSerializer
	permission_classes = (IsAuthenticated, )

	def perform_create(self, serializer):
		project = Project.objects.get(id=int(self.request.data.get("project")))
		serializer.save(project=project)


class ColumnDetailView(generics.RetrieveUpdateDestroyAPIView):
	serializer_class = ColumnDetailSerializer
	queryset = Column.objects.all()
	permission_classes = (IsAuthenticated, IsOwnerReadOnly)

