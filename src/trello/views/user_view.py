from rest_framework import generics
from trello.permissions import *
from trello.models import *
from rest_framework.permissions import IsAuthenticated
from trello.serializers.subtask_serializers import *


class UserListView(generics.ListAPIView):
	"""

	"""
	serializer_class = UserListView
	queryset = User.objects.all()
	permission_classes = (IsAuthenticated, IsOwnerOrManagerForProject)

	def get_queryset(self):
		project = self.request.data.project
		owner = Project.objects.get(owner_project=project)
		managers = Project.objects.filter(manager_project=project)
		return (owner, managers)
