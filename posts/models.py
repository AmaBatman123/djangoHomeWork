from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=56)
    content = models.TextField()
    rate =models.IntegerField(null=True,blank=True)
    created_at = models.DateTimeField(null=True, auto_now_add=True)
    updated_at = models.DateTimeField(null=True, auto_now=True)

    def __str__(self):
        return f"{self.title}: {self.content}"
