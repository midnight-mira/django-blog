from django.urls import path
from posts.views import PostCreateView

urlpatterns = [
    path("new-post/", PostCreateView.as_view(), name="create_post")
]
