from django.shortcuts import render
from rest_framework import generics
from rest_framework.generics import get_object_or_404
from .serializers import *
from .permissions import *
from rest_framework.permissions import IsAuthenticated, IsAdminUser


class ProjectDetailView(generics.RetrieveUpdateDestroyAPIView):
	serializer_class = ProjectDetailSerializer
	queryset = Project.objects.all()
	permission_classes = (IsAuthenticated, )

	def get_object(self):
		obj = get_object_or_404(self.queryset, user=self.request.user)
		return obj


class ProjectCreateView(generics.CreateAPIView):
	serializer_class = ProjectDetailSerializer
	permission_classes = (IsAuthenticated, )

	def perform_create(self, serializer):
		serializer.save(user=self.request.user)


class ProjectListSerializer(generics.ListAPIView):
	serializer_class = ProjectListSerializer
	queryset = Project.objects.all()
	permission_classes = (IsAuthenticated, )

	def get_queryset(self):
		user = self.request.user
		return Project.objects.filter(user=user)

# ====================================================================================================


class ColumnCreateView(generics.CreateAPIView):
	serializer_class = ColumnDetailSerializer
	permission_classes = (IsAuthenticated, )

	def perform_create(self, serializer):
		serializer.save(project=self.request.project)


class TaskCreateView(generics.CreateAPIView):
	serializer_class = TaskDetailSerializer
	permission_classes = (IsAuthenticated, )

	def perform_create(self, serializer):
		serializer.save(owner=self.request.user)
		serializer.save(column=self.request.column)


class SubtaskCreateView(generics.CreateAPIView):
	serializer_class = SubtaskDetailSerializer
	permission_classes = (IsAuthenticated,)

	def perform_create(self, serializer):
		serializer.save(owner=self.request.user)
		serializer.save(task=self.request.task)


class CommentCreateView(generics.CreateAPIView):
	serializer_class = CommentDetailSerializer
	permission_classes = (IsAuthenticated,)

	def perform_create(self, serializer):
		serializer.save(owner=self.request.user)

# ==========================================================================================================


class ColumnDetailView(generics.RetrieveUpdateDestroyAPIView):
	serializer_class = ColumnDetailSerializer
	queryset = Column.objects.all()
	permission_classes = (IsAuthenticated, IsOwnerReadOnly, IsAdminUser)


class TaskDetailView(generics.RetrieveUpdateDestroyAPIView):
	serializer_class = TaskDetailSerializer
	queryset = Task.objects.all()
	permission_classes = (IsAuthenticated, IsOwnerReadOnly, IsAdminUser)


class SubtaskDetailView(generics.RetrieveUpdateDestroyAPIView):
	serializer_class = SubtaskDetailSerializer
	queryset = Subtask.objects.all()
	permission_classes = (IsAuthenticated, IsOwnerReadOnly, IsAdminUser)


class CommentDetailView(generics.RetrieveUpdateDestroyAPIView):
	serializer_class = CommentDetailSerializer
	queryset = Comment.objects.all()
	permission_classes = (IsAuthenticated, IsOwnerReadOnly, IsAdminUser)



