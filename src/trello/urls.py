from django.contrib import admin
from django.urls import path, include
from .views import *


urlpatterns = [
	path('project/detail/', ProjectDetailView.as_view()),
	path('project/create/', ProjectCreateView.as_view()),
	path('project/all/', ProjectListSerializer.as_view()),

	path('project/column/<int:pk>/', ColumnDetailView.as_view()),
	path('project/column/task/<int:pk>/', TaskDetailView.as_view()),
	path('project/column/task/subtask/<int:pk>/', SubtaskDetailView.as_view()),
	path('project/column/task/comment/<int:pk>/', CommentDetailView.as_view()),

	path('project/column/create/', ColumnCreateView.as_view()),
	path('project/column/task/', TaskCreateView.as_view()),
	path('project/column/task/subtask/', SubtaskCreateView.as_view()),
	path('project/column/task/comment/', CommentCreateView.as_view()),

]