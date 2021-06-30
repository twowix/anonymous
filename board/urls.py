from django.urls import path
from board.views import board, post_detail, post_write

urlpatterns = [
    path('', board, name='board'),
    path('post', post_write, name="post_write"),
    path('post/<int:post_id>', post_detail, name="post_detail"),
]
