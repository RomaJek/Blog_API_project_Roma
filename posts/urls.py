from django.urls import path
from .views import PostListView, PostDetailView, CategoryListView, CategoryDetailView, TagListView, TagDetailView

urlpatterns = [
    path('posts/', PostListView.as_view(), name='post-list'),
    path('posts/<int:post_id>/', PostDetailView.as_view(), name='post-detail'),
    path('categories/', CategoryListView.as_view(), name='category-list'),
    path('categories/<int:category_id>/', CategoryDetailView.as_view(), name='category-detail'),
    path('tags/', TagListView.as_view(), name='tag-list'),
    path('tags/<int:tag_id>/', TagDetailView.as_view(), name='tag-detail'),
]