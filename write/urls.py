from django.contrib import admin
from django.urls import path
import write.views

urlpatterns = [
    path('home/', write.views.home, name='home'),
    path('post/<int:post_id>/', write.views.detail, name='detail'),
    path('post/new/', write.views.post_new, name='new'),
    path('post/<int:post_id>/edit', write.views.post_edit, name='edit'),
    path('post/<int:post_id>/delete', write.views.post_delete, name='delete'),
    path('post/<int:post_id>/comment', write.views.add_comment, name='add_comment'),
    path('comment/<int:comment_id>/delete', write.views.comment_delete, name='comment_delete'),
]