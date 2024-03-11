## config/authentication.py

# REST framework에서 제공하는 기본 인증 시스템
from rest_framework.authentication import BaseAuthentication
# 디코드
import jwt
# 시크릿키
from django.conf import settings
from users.models import User

class JWTAuthentication(BaseAuthentication):
    def authenticate(self, request):
        token = request.headers.get("jwt-auth") # jwt-token
        
        if not token:
            return None
        
        # 토큰이 존재한다면 디코드
        # HS256은 업계 표준 알고리즘
        decoded = jwt.decode(token, settings.SECRET_KEY, algorithms=["HS256"])
        user_id = decoded.get('id')
        user = User.objects.get(id=user_id)
        
        return (user, None) # user,token을 넘겨주지만 필요없는 토큰은 받아오지않는다.