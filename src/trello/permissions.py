from rest_framework import permissions


class IsOwnerOrManagerForProject(permissions.BasePermission):
	def has_object_permission(self, request, view, obj):
		return obj.owner == request.user or request.user in obj.managers.all()


class IsOwnerOrManagerForColumn(permissions.BasePermission):
	def has_object_permission(self, request, view, obj):
		return obj.project.owner == request.user or request.user in obj.project.managers.all()


class IsOwnerOrManagerForTask(permissions.BasePermission):
	def has_object_permission(self, request, view, obj):
		return obj.column.project.owner == request.user or request.user in obj.column.project.managers.all()


class IsOwnerOrManagerForSubtaskOrAttachmentsOrComment(permissions.BasePermission):
	def has_object_permission(self, request, view, obj):
		return obj.task.column.project.owner == request.user or request.user in obj.task.column.project.managers.all()
