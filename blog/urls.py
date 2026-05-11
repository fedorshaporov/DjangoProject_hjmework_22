from django.urls import path
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView

app_name = 'blog'

urlpatterns = [
    path('', PostListView.as_view(), name='post_list'),  # Заканчивается на /
    path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),  # Заканчивается на /
    path('post/new/', PostCreateView.as_view(), name='post_create'),  # Заканчивается на /
    path('post/<int:pk>/edit/', PostUpdateView.as_view(), name='post_edit'),  # Заканчивается на /
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),  # Заканчивается на /
]