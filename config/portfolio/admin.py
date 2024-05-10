from django.contrib import admin
from .models import Author, Message

admin.site.register(Author)
admin.site.register(Message)