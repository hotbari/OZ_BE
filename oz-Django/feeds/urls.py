# feeds/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path("", views.show_feed),
    path("all", views.all_feed),
<<<<<<< HEAD
    path("<int:feed_id>/<str:feed_content>/", views.one_feed),
]
=======
    path("<int:feed_id>/<str:feed_content>/", views.one_feed)
]
>>>>>>> refs/remotes/origin/main
