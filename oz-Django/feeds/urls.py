## feeds/urls.py

from django.urls import path
from . import views

urlpatterns = [
    # 전체게시글 조회이기때문에 루트경로로 입력
    # .as_view()는 APIView와 url을 맵핑시켜주는 함수
    path("",views.Feeds.as_view()),
    path("<int:feed_id>",views.FeedDetail.as_view())
]
