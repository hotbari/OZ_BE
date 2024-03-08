from typing import Any, Optional
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin
)

from django.db import models

class UserManager(BaseUserManager):
    '''
    user 모델을 관리해주는 클래스 (보통 생성 담당)
    비밀번호 관리
    '''
    use_in_migrations = True
    
    def create_user(
        self,
        user_id:str,
        email:str,
        gender:str,
        password:Optional[str],
        **kwargs:Any) -> "User":
        
        if not user_id:
            raise ValueError('아이디를 입력하세요')
        user:"User" = self.model(
            user_id=user_id,
            email=email,
            gender=gender
        )
        user.set_password(password)
        user.save(using = self._db)
        return user
    
    
    def create_superuser(
        self,
        user_id:str,
        email:str,
        gender:str,
        password:Optional[str],
        **kwargs:Any) -> "User":
        user: "User" = self.create_user(
            user_id=user_id,
            email=email,
            gender=gender,
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user
        


class User(AbstractBaseUser, PermissionsMixin):
    
    class GenderChoice(models.TextChoices):
        '''
        성별을 선택하게 하는 모델
        index[1] : 보여지는 값
        index[0] : 실제 DB에 저장되는 값
        '''
        MALE = ('male', 'Male')
        FEMALE = ('female', 'female')
        
        
    user_id = models.CharField(max_length=20, unique=True)
    email = models.EmailField(max_length=100,unique=True)
    gender = models.CharField(max_length=7, choices = GenderChoice.choices)
    # 2차 인증이 필요한 회원가입의 경우 등에는 False가 default로
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True) # 생성하는 시간만 한 번 저장
    updated_at = models.DateTimeField(auto_now=True) # 업데이트 할 때마다 시간 저장
    
    
    objects = UserManager()
    
    
    # 현재는 디폴트값인 username이 없어서 읽지 못함
    # USERNAME_FIELD = 'username'
    
    USERNAME_FIELD = 'user_id'
    
    class Meta:
        db_table = 'users'
        