from django.db import models

class Book(models.Model):
    book_name = models.CharField(max_length=30)

