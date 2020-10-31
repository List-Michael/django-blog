from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length=128)
    text = models.TextField(blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_date = models.DateTimeField.auto_now_add()
    modified_date = models.DateTimeField.auto_now()
    published_date = models.DateTimeField(blank=True, null=True)
    score = models.IntegerField(default=0)
