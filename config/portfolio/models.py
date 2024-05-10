from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=15)
    lastname = models.CharField(max_length=15)
    about = models.TextField()
    image = models.ImageField(upload_to='author')

    class Meta:
        ordering = ['-id']
        verbose_name = 'Author'
        verbose_name_plural = 'The author'

    def __str__(self):
        return f'{self.name} {self.lastname}'


class Message(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Message'
        verbose_name_plural = 'Messages'

    def __str__(self):
        return f'Message from {self.name}: {self.subject}'   
