from django.db import models
from books.models import Book
# from users.models import User


class Spoiler(models.Model):
    writer = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    content = models.TextField()
    
    book_id = models.ForeignKey(Book, on_delete=models.CASCADE)
    # user_id = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title