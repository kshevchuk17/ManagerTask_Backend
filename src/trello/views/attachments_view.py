from django.shortcuts import render
from rest_framework import generics
from rest_framework.generics import get_object_or_404
from trello.permissions import *
from trello.models import *
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from trello.serializers.attachments_serializers import *


class AttachmentCreateView(generics.CreateAPIView):
	serializer_class = AttachmentDetailSerializer
	permission_classes = (IsAuthenticated, )

	def perform_create(self, serializer):
		serializer.save(task=self.request.task)


class AttachmentDetailView(generics.RetrieveUpdateDestroyAPIView):
	serializer_class = AttachmentDetailSerializer
	queryset = Attachment.objects.all()
	permission_classes = (IsAuthenticated, )

