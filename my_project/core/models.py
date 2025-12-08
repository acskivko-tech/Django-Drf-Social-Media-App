from django.db import models

from users.models import CustomUser


# Create your models here.

"""Model for genre messages"""
class Genre(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    def __str__(self):
        return self.name


"""Models blog messages"""
class Post(models.Model):
    title = models.CharField(
        max_length=100
    )

    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE,related_name='posts')

    content = models.TextField(
        blank=True,
    )

    date = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:
        ordering = ['-date']

    genre = models.ForeignKey(
        Genre,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='messages')

    def __str__(self):
        return f"{self.title} ({self.author})"