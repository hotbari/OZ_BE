## reviews.views.py

from django.shortcuts import render
from .models import Review
from .serializers import ReviewSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.exceptions import NotFound, NotAuthenticated

# 전체 댓글 조회
class Reviews(APIView):
    def get(self, request):
        reviews = Review.objects.all()
        
        # 시리얼라이즈
        serializer = ReviewSerializer(reviews, many=True) # 리뷰가 여러개
        return Response(serializer.data)

# 특정 아이디 댓글만 조회
class ReviewsDetail(APIView):
    def get(self, request, review_id):
        try:
            review = Review.objects.get(id=review_id)
        except Review.DoesNotExist:
            raise NotFound
        
        serializer = ReviewSerializer(review)
        return Response(serializer.data)
    