from django.urls import path
from .views import PostLists, PostDetail

urlpatterns = [
    path("", PostLists.as_view(), name = 'posts_list'),
    path("<int:pk>/", PostDetail.as_view(), name = 'posts_detail'),
]