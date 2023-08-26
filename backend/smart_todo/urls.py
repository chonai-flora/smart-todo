from django.contrib import admin
from rest_framework import routers
from django.urls import path, include
from rest_framework import routers

from . import views

router = routers.SimpleRouter()
router.register('projects', views.ProjectView)
router.register('members', views.MemberView)
router.register('todos', views.TodoView)
router.register('todos/<str:project_id>', views.TodoView)

urlpatterns = [
    path('', include(router.urls))
]