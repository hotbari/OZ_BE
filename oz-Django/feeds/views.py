## feeds/views.py

from django.shortcuts import render
# RestFramework에서 제공하는 APIView를 사용
from rest_framework.views import APIView
from .models import Feed
# 만든 시리얼라이즈 import
from .serializers import FeedSerializer
from rest_framework.response import Response
# NotFound import
from rest_framework.exceptions import NotFound


# Create your views here
class Feeds(APIView):
    # 전체 게시글 조회
    def get(self, request):
        # 전체 객체데이터를 가짐
        feeds = Feed.objects.all()
        
        # 객체 -> JSON (시리얼라이즈)
        # ModelSerializer가 상속된 FeedSerializer 클래스가 다수의 feeds객체를 직렬화 할것이라는 의미
        serializer = FeedSerializer(feeds, many=True)
        # 직렬화된 데이터를 반환
        return Response(serializer.data)
    
    # 유저가 보낸 request를 다룸
    def post(self, request):
        # 역직렬화 (클라이언트가 보내준 json -> object 형태로 변경)
        serializer = FeedSerializer(data=request.data)
        
        # 시리얼라이저 클래스에서 정의된 유효성 검사 규칙에 데이터가 준수하면 True 반환
        if serializer.is_valid():
            feed = serializer.save(user=request.user)
        
            serializer = FeedSerializer(feed)
            return Response(serializer.data)
        else :
            return Response(serializer.errors)
        
        
class FeedDetail(APIView):
    def get_object(self, feed_id):
        try:
            return Feed.objects.get(id=feed_id)
        # feed가 존재하지 않을 경우
        except Feed.DoesNotExist :
            raise NotFound
    
    def get(self, request, feed_id): 
        feed = self.get_object(feed_id) #self를 통해 클래스 내 인스턴스에 접근
        # feed를 시리얼라이징
        serializer = FeedSerializer(feed)
        # 결과를 HTTP 응답으로 반환
        return Response(serializer.data)