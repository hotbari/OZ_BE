## users/veiws.py

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import NotFound, ParseError
from .models import User
from .serializers import MyInfoUserSerializer
from django.contrib.auth.password_validation import validate_password

# 토큰
from rest_framework.authentication import TokenAuthentication # 유저식별(사용자 인증)
from rest_framework.permissions import IsAuthenticated # 권한부여

# 세션 로그인
from django.contrib.auth import authenticate, login
from rest_framework import status

#[POST] 유저 생성 API
# api/v1/users 
class Users(APIView):
    def post(self, request):
        # password(검증->해쉬화->저장)
        password = request.data.get('password')
        serializer = MyInfoUserSerializer(data=request.data)
        
        try:
            validate_password(password)
        except:
            raise ParseError("Invalid password")
        
        if serializer.is_valid():
            user = serializer.save()
            user.set_password(password)
            user.save()
            
            serializer = MyInfoUserSerializer(user)
            return Response(serializer.data)
        
        else:
            raise ParseError(serializer.errors)
        # the other
        

#[GET, PUT] 데이터 업데이트
# api/v1/users/myinfo
class MyInfo(APIView):
    
    # 데코레이터를 적용해서 토큰데이터에 정보 접근 제한
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    
    
    
    def get(self, request):
        user = request.user
        serializer = MyInfoUserSerializer(user)
        
        return Response(serializer.data)
    
    def put(self, request):
        user = request.user
        serializer = MyInfoUserSerializer(user,
                                          data=request.data, # 업데이트하려는 데이터
                                          partial=True) # 모델의 인스턴스가 일부만 있는 경우에도 허용
        
        if serializer.is_valid():
            user = serializer.save()
            serializer = MyInfoUserSerializer(user)
            return Response(serializer.data)
        
        else:
            return Response(serializer.errors)
        
        
# api/v1/users/login
# GET은 보안에 취약하기 때문에 POST로
class Login(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        
        if not username or not password :
            raise ParseError()
        
        user = authenticate(request, username=username, password=password)
        
        if user:
            login(request, user)
            
            return Response(status=status.HTTP_200_OK)
        
        else :
            return Response(status=status.HTTP_403_FORBIDDEN)
        
from django.contrib.auth import logout        
class Logout(APIView):
    # 실제로 로그인한 유저인지 확인
    permission_classes = [IsAuthenticated]
    
    def post(self, request):
        logout(request)
        
        return Response(status=status.HTTP_200_OK)
    
    

# 토큰 생성

import jwt
from django.conf import settings

class JWTLogin(APIView):
    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")
        
        if not username or not password:
            raise ParseError()
        
        user = authenticate(request, username=username, password=password)
        
        if user:
            payload = {"id":user.id, "username":user.username} # user을 구분할 수 있는 값
            token = jwt.encode(
                payload,
                settings.SECRET_KEY,
                algorithm="HS256"
            )
            
            return Response({"token":token})
        
        
# 토큰 검증
from config.authentication import JWTAuthentication
class UserDetailView(APIView):
    # authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        user = request.user
        
        return Response({"id":user.id,"username":user.username})