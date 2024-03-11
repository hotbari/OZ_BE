## users.serializers.py

from rest_framework.serializers import ModelSerializer
from .models import User

class FeedUserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ("username","email",)
        
        
## User API에 필요할 시리얼라이저 생성
class MyInfoUserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"