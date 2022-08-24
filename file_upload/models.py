from django.db import models

# Create your models here.
from authentication.models import User


class Post(models.Model):
    user_id = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='user')
    id = models.AutoField(unique=True, primary_key=True)
    title = models.CharField(max_length=1024, null=False, blank=False)
    body = models.CharField(max_length=3072, null=False, blank=False)
