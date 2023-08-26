from django import forms
from .models import *


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ('name',)


class MemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ('name',)


class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ('title', 'description', 'deadline', 'completed', 'project', 'members')