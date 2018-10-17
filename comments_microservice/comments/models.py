from django.db import models

class Comment(models.Model):
    author = models.ForeignKey('auth.User', related_name='comments', on_delete=models.CASCADE)
    title = models.CharField(max_length=128)
    text = models.CharField(max_length=128)
    created = models.DateTimeField(auto_now_add=True)
    edited = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return self.title
