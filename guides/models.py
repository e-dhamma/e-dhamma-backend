from django.db import models

class Guide(models.Model):
    header = models.CharField(max_length=200)
    content = models.TextField()
