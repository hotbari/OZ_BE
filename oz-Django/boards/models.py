from django.db import models
from django.utils import timezone

#CommonModel import
from common.models import CommonModel


# Create your models here.
class Board(CommonModel):
    title = models.CharField(max_length=30)
    content = models.TextField()
    date = models.DateTimeField(default=timezone.now)
    likes = models.PositiveBigIntegerField(default=0)
    reviews = models.PositiveBigIntegerField(default=0)
    writer = models.CharField(max_length=30)
    
    # FK 연결
    # user 데이터가 삭제되면 Board 데이터도 삭제
    user = models.ForeignKey("users.User",on_delete=models.CASCADE)

    # 제목 보여주기
    def __str__(self):
        return self.title
