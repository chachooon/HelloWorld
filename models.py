from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=40)

class Post(models.Model):
    category = models.ForeignKey(Category)
    title = models.CharField(max_length=200)
    content = models.TextField()
    tags = models.ManyToManyField('Tag')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return '{} - {}'.format(self.pk, self.title)

class Comment(models.Model):
    post = models.ForeignKey(Post)
    content = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Tag(models.Model):
    name = models.CharField(max_length=40)
    def __str__(self):
        return self.name
