from django.db import models

# Create your models here.
class Todo_list(models.Model):
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=30)
    complete = models.BooleanField(default=False)
    user_id = models.CharField(max_length=10)