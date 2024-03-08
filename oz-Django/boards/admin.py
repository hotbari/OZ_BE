from django.contrib import admin
from .models import Board  # models 폴더에서 Board를 import


# 모델 등록
@admin.register(Board)
class BoardAdmin(admin.ModelAdmin):
    # 관리자 페이지 목록에 표시할 필드 지정
    list_display = (
        "title",
        "date",
        "likes",
        "content",
        "created_at",
        "updated_at"
    )

    # 필터 옵션으로 사용한 필드 지정
    list_filter = ("date",)

    # 검색 기능에 사용할 필드 지정
    search_fields = (
        "title",
        "content",
    )

    # 목록페이지 기본 정렬 순서
    # 최근순
    ordering = ("-date",)

    # 읽기 전용 필드 지정, 사용자가 편집 불가
    readonly_fields = ("writer",)

    # 상세페이지에서 필드 그룹을 어떻게 나눌지 지정
    # 사용자를 등록할 때, 숨겨진 옵션창이 하단의 형태로 생성된다.
    # title, content 필드는 기본 노출, writer, likes, revies 필드는 숨겨진 상태
    fieldsets = (
        (None, {"fields": ("title", "content")}),
        (
            "Advanced options",
            {"fields": ("writer", "likes", "reviews"), "classes": ("collapse",)},
        ),
    )

    # 목록페이지에 표시할 항목 수 지정
    list_per_page = 1

    # 사용자 정의 대량 작업 추가
    # 좋아요 수 증가
    actions = ("increment_likes",)

    def increment_likes(self, request, queryset):
        # 선택된 게시글들에 대해 'likes' 수를 1씩 증가
        for board in queryset:
            board.likes += 10
            board.save()

    increment_likes.short_description = "likes +10"
