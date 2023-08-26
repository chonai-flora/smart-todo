from rest_framework import serializers
from .models import *


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('name',)


class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = ('name',)


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ('title', 'description', 'deadline', 'completed', 'project', 'members')