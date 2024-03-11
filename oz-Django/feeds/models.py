## feeds/models.py

from django.db import models

#CommonModel을 상속받기위해 불러옴
from common.models import CommonModel

# Create your models here.
# 제목(title), 내용(content), 작성자(User)
# User:Feed = 1:N 
# Feed가 User를 FK로 가짐

class Feed(CommonModel):
    title = models.CharField(max_length=30)
    content = models.CharField(max_length=120)
    
    # User가 삭제되면 Feed도 삭제되도록 옵션 설정
    user = models.ForeignKey("users.User", on_delete=models.CASCADE)
    
    
