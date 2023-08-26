from django.views import generic
from django.shortcuts import render
from django.urls import reverse_lazy
from django.http import HttpResponse
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Project, Member, Todo
from .forms import ProjectForm, MemberForm, TodoForm
from .serializers import ProjectSerializer, MemberSerializer, TodoSerializer

class ProjectView(viewsets.ModelViewSet):
    serializer_class = ProjectSerializer
    queryset = Project.objects.all()


class MemberView(viewsets.ModelViewSet):
    serializer_class = MemberSerializer
    queryset = Member.objects.all()


class TodoView(viewsets.ModelViewSet):
    serializer_class = TodoSerializer
    queryset = Todo.objects.all()

    def list(self, request):
        todos = Todo.objects.filter(project_id=request.GET.get('project_id'))
        serializer = TodoSerializer(todos, many=True)
        return Response(serializer.data)