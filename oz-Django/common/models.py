from django.db import models

# Create your models here.
class CommonModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True) # 생성시간 기준
    updated_at = models.DateTimeField(auto_now=True) # 업데이트시간 기준
    
    # Meta클래스는 모델에 대한 다양한 사항을 정의
    # DB 테이블에 추가하지 않음 -> 전체 테이블에 created_at, updated_at 필드가 들어가면 복잡해지기때문
    # 추상기반 클래스임을 나타냄
    class Meta:
        abstract = True 
    