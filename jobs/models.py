from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=250, blank=True)
    added_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Job(models.Model):
    title = models.CharField(max_length=250)
    summary = models.CharField(max_length=500)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    added_by = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    added_at = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField()

    def __str__(self) -> str:
        return self.title


class Application(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    applicant = models.ForeignKey(User, on_delete=models.CASCADE)
    applied_at = models.DateTimeField(auto_now_add=True)
    description = models.TextField()
    resume = models.FileField(upload_to='jobs/resume')
    
