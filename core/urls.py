from django.urls import path, include

from . import views
from .views import ThreadListView, ThreadCreateView, ThreadUpdateView, DeleteThread, CommentCreateView, CommentUpdateView, DeleteComment

urlpatterns = [
    path('', ThreadListView.as_view(), name='home'),
    #path('user/<str:username>', UserThreadListView.as_view(), name='user-threads'),
    path('thread/new/', ThreadCreateView.as_view(), name='thread-create'),
    path('thread/<int:pk>/update/', ThreadUpdateView.as_view(), name='thread-update'),
    path('thread/<int:pk>/delete/', DeleteThread, name='thread-delete'),
    path('comment/new/', CommentCreateView.as_view(), name='comment-create'),
    path('comment/<int:pk>/update/', CommentUpdateView.as_view, name='comment-update'),
    path('comment/<int:pk>/delete/', DeleteComment, name='comment-delete')
]
