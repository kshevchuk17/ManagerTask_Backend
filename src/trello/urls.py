from django.contrib import admin
from django.urls import path, include
from .views.project_view import *
from .views.column_view import *
from .views.task_view import *
from .views.subtask_view import *
from .views.comment_view import *
from .views.attachments_view import *


urlpatterns = [
	path('project/detail/<int:pk>/', ProjectDetailView.as_view()),
	path('project/create/', ProjectCreateView.as_view()),
	path('project/all/', ProjectListSerializer.as_view()),
	path('project/add_manager/', ProjectAddManagerView.as_view()),

	path('project/column/<int:pk>/', ColumnDetailView.as_view()),
	path('project/column/task/<int:pk>/', TaskDetailView.as_view()),
	path('project/column/task/subtask/<int:pk>/', SubtaskDetailView.as_view()),
	path('project/column/task/comment/<int:pk>/', CommentDetailView.as_view()),
	path('project/column/task/attachment/<int:pk>/', AttachmentDetailView.as_view()),

	path('project/column/create/', ColumnCreateView.as_view()),
	path('project/column/task/create/', TaskCreateView.as_view()),
	path('project/column/task/subtask/create/', SubtaskCreateView.as_view()),
	path('project/column/task/comment/create/', CommentCreateView.as_view()),
	path('project/column/task/attachment/create/', AttachmentCreateView.as_view()),

]