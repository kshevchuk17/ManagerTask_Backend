from django.contrib import admin
from django.urls import path, include
from .views import *


urlpatterns = [
	path('project/detail/', ProjectDetailView.as_view()),
	path('project/create/', ProjectCreateView.as_view()),
	path('project/all/', ProjectListSerializer.as_view())
]