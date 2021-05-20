from django.shortcuts import render
from rest_framework import generics
from rest_framework.generics import get_object_or_404
from trello.permissions import *
from trello.models import *
from rest_framework.permissions import IsAuthenticated
from trello.serializers.comments_serializers import *


class CommentCreateView(generics.CreateAPIView):
	serializer_class = CommentDetailSerializer
	permission_classes = (IsAuthenticated,IsOwnerOrManagerForSubtaskOrAttachmentsOrComment)

	def perform_create(self, serializer):
		serializer.save(owner=self.request.user)


class CommentDetailView(generics.RetrieveUpdateDestroyAPIView):
	serializer_class = CommentDetailSerializer
	queryset = Comment.objects.all()
	permission_classes = (IsAuthenticated, IsOwnerOrManagerForSubtaskOrAttachmentsOrComment)
