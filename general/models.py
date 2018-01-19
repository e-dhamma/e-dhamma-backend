from django.db import models

class LetterToAdmin (models.Model):
    name = models.CharField(max_length=250)
    email = models.EmailField()
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    solved = models.BooleanField(default=False)

