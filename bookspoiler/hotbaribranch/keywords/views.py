from django.shortcuts import render
from .serializers import KeywordSerializer
from rest_framework import generics
from rest_framework.exceptions import NotFound
from .models import Keyword
from books.models import Book

# 전체 키워드 목록 조회
class KeywordList(generics.ListAPIView):
    queryset = Keyword.objects.all()
    serializer_class = KeywordSerializer

# 생성하기
class CreateKeyword(generics.CreateAPIView):
    serializer_class = KeywordSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


# 개별 수정 및 불러오기
class KeywordDetail(generics.RetrieveUpdateAPIView):

    serializer_class = KeywordSerializer
    queryset = Keyword.objects.all()

    def handle_exception(self, exc):
        if isinstance(exc, NotFound):
            return Response({"detail":"Not Found."}, status=HTTP_404_NOT_FOUND)
        return super().handle_exception(exc)