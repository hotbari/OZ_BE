from django.shortcuts import render
from rest_framework import generics
from .serializers import SpoilerSerializer
from .models import Spoiler
from rest_framework.exceptions import NotFound

# 생성하기
class CreateSpoiler(generics.CreateAPIView):
    serializer_class = SpoilerSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


# 수정 및 불러오기
class SpoilerDetail(generics.RetrieveUpdateAPIView):

    serializer_class = SpoilerSerializer
    queryset = Spoiler.objects.all()

    def handle_exception(self, exc):
        if isinstance(exc, NotFound):
            return Response({"detail":"Not Found."}, status=HTTP_404_NOT_FOUND)
        return super().handle_exception(exc)