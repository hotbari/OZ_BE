from django.db import models
from books.models import Book

class Review(models.Model):
    url = models.URLField()
    writer = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    content = models.TextField()
    type = models.CharField(max_length=255)
    
    book_id = models.ForeignKey(Book, on_delete=models.CASCADE)

    def __str__(self):
        return self.title