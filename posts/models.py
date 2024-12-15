from django.db import models

class Category(models.Model):
    title = models.CharField(max_length=56)

    def __str__(self):
        return self.title

class Tag(models.Model):
    title = models.CharField(max_length=56)

    def __str__(self):
        return self.title

class Post(models.Model):
    title = models.CharField(max_length=56)
    content = models.TextField()
    rate =models.IntegerField(null=True,blank=True)
    created_at = models.DateTimeField(null=True, auto_now_add=True)
    updated_at = models.DateTimeField(null=True, auto_now=True)
    image = models.ImageField(null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    tags = models.ManyToManyField(Tag, null=True, blank=True)

    def __str__(self):
        return f"{self.title}: {self.content}"


