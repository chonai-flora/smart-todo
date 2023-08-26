import uuid as uuid_lib
from django.db import models


class Project(models.Model):
    id = models.UUIDField(default=uuid_lib.uuid4, editable=False, primary_key=True)
    name = models.CharField(max_length=255)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Member(models.Model):
    id = models.UUIDField(default=uuid_lib.uuid4, editable=False, primary_key=True)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    

class Todo(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    members = models.ManyToManyField('Member')

    id = models.UUIDField(default=uuid_lib.uuid4, editable=False, primary_key=True)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    deadline = models.DateField(auto_now=False)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title