"""
URL configuration for hotbaribranch project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from books import views as books_views
from keywords import views as keywords_views
from spoilers import views as spoiler_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path("books/", books_views.Books.as_view()), # 등록완료 상태인 도서 리스트 불러오기
    path("books/all/", books_views.BookList.as_view()), # 전체 도서 리스트 불러오기
    path("book/create/", books_views.BookCreate.as_view()), # 신규 도서 생성하기
    path("book/<int:pk>/", books_views.BookDetail.as_view()), # 개별 도서 리스트 관리 및 개별 도서 정보 수정하기
    path("<int:challenge_info_id>/", include("challenge_spoilers.urls")), # 챌린지 스포일러 관리
    path("keywords/", keywords_views.KeywordList.as_view()), # 전체 키워드 조회
    path("keyword/", include("keywords.urls")), # 개별 키워드 관리
    path("review/", include("reviews.urls")), # 추천 서평 관리
    path("book/<int:book_id>/spoiler/", include("spoilers.urls")), # 일반 스포일러 관리
]
