from django.shortcuts import render
from rest_framework import generics
from .serializers import ReviewSerializer
from .models import Review
from rest_framework.exceptions import NotFound

# 생성하기
class CreateReview(generics.CreateAPIView):
    serializer_class = ReviewSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


# 수정 및 불러오기
class ReviewDetail(generics.RetrieveUpdateAPIView):

    serializer_class = ReviewSerializer
    queryset = Review.objects.all()

    def handle_exception(self, exc):
        if isinstance(exc, NotFound):
            return Response({"detail":"Not Found."}, status=HTTP_404_NOT_FOUND)
        return super().handle_exception(exc)