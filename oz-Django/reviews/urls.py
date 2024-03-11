## reviews/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path("", views.Reviews.as_view()),
    path("<int:review_id>", views.ReviewsDetail.as_view()),
]
