# users/urls.py

from django.urls import path
from . import views

# 토큰
from rest_framework.authtoken.views import obtain_auth_token

# Simple JWT
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
		TokenVerifyView
)

urlpatterns = [
    path("", views.Users.as_view()), # 주소: api/v1/users
    path("myinfo", views.MyInfo.as_view()), # 주소: api/v1/users/myinfo
    
    #Authentication
    path("getToken", obtain_auth_token), #Django REST framwork Token
    path("login", views.Login.as_view()), # Django Session Login
    path("logout", views.Logout.as_view()), # Django Session Logout
    
    # JWT Authentication
    path("login/jwt", views.JWTLogin.as_view()),
    path("login/jwt/info", views.UserDetailView.as_view()),
    
    # Simple JWT
    path("login/simplejwt", TokenObtainPairView.as_view()),
    path("login/simplejwt/refresh", TokenRefreshView.as_view()),
    path("login/simplejwt/verify", TokenVerifyView.as_view())
    
]

'''
{
    "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcxMTM1ODM1OCwiaWF0IjoxNzEwMTQ4NzU4LCJqdGkiOiI5NzFmOTgxZmQ2NWI0MGRjOWE1NDQyYTcwYzhkNTJmNSIsInVzZXJfaWQiOjF9.j4jkRyAJS-J0Oyr2gK7vPCiu9PuKfjA95LLre0MpNr8",
    "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzEwMTUyMzU4LCJpYXQiOjE3MTAxNDg3NTgsImp0aSI6IjgwNjE2NmM2OTRjNTQyMTY5NjYzMTFkMDY4ZGY5NzE1IiwidXNlcl9pZCI6MX0.CrmIybx4-bN3OHXVcC-8SymnS5KH5AKEOJqWTdmKbos"
}
'''
