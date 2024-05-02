from django.shortcuts import render
from rest_framework import generics
from .serializers import ChallengeSpoilerSerializer
from .models import ChallengeSpoiler
from rest_framework.exceptions import NotFound

# 생성하기
class CreateChallengeSpoiler(generics.CreateAPIView):
    serializer_class = ChallengeSpoilerSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


# 수정 및 불러오기
class ChallengeSpoilerDetail(generics.RetrieveUpdateAPIView):

    serializer_class = ChallengeSpoilerSerializer
    queryset = ChallengeSpoiler.objects.all()

    def handle_exception(self, exc):
        if isinstance(exc, NotFound):
            return Response({"detail":"Not Found."}, status=HTTP_404_NOT_FOUND)
        return super().handle_exception(exc)