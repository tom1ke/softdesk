from django.db import models
from django.forms import fields
from django.contrib.auth import get_user_model


class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=2000, blank=True)
    type = models.CharField(max_length=100)
    author = models.ForeignKey(to=get_user_model(), on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Contributor(models.Model):
    user = models.ForeignKey(to=get_user_model(), on_delete=models.CASCADE)
    project = models.ForeignKey(to=Project, on_delete=models.CASCADE)
    permission = fields.ChoiceField
    role = models.CharField(max_length=100)


class Issue(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=2000, blank=True)
    tag = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
    date_created = models.DateTimeField(auto_now_add=True)
    project = models.ForeignKey(to=Project, on_delete=models.CASCADE, related_name='issues')
    author = models.ForeignKey(to=get_user_model(), on_delete=models.CASCADE)
    assignee = models.ForeignKey(to=get_user_model(), null=True, on_delete=models.SET_NULL, related_name='assignees')

    def __str__(self):
        return self.title


class Comment(models.Model):
    content = models.TextField(max_length=2000)
    date_created = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(to=get_user_model(), on_delete=models.CASCADE)
    issue = models.ForeignKey(to=Issue, on_delete=models.CASCADE, related_name='comments')

    def __str__(self):
        return self.author
