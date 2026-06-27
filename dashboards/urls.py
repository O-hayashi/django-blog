from django.urls import path, include
from . import views

urlpatterns = [
  path('', views.dashboard, name='dashboard'),
  path('categories/', views.categories, name='categories'),
  path('categories/add/', views.add_category, name='add_category'),
  path('categories/edit/<int:pk>/', views.edit_category, name='edit_category'),
  path('categories/delete/<int:pk>', views.delete_category, name='delete_category'),
  # url patterns for dashboard-blog-posts
  path('posts/', views.posts, name='posts'),
  path('posts/add/', views.add_post, name='add_post'),
  path('post/delete/<int:pk>/', views.delete_post, name='delete_post'),
  path('posts/edit/<int:pk>/', views.edit_post, name='edit_post'),

]      