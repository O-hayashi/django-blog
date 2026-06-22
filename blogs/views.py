from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Blog, Category

def posts_by_category(request, category_id):
  posts = Blog.objects.filter(category_id = category_id, status = 'Published')
  # try:
  #   category = Category.objects.get(id = category_id)
  # except:
  #   return redirect('home')
  # we can also use get_object_or_404 to show the 404 error page if the category doesnt't exist or try except block if we wanna do some custom action if the category doesn't exist
  category = get_object_or_404(Category, pk = category_id)
  context = {
    'posts': posts,
    'category': category,
  }
  return render(request, 'posts_by_category.html', context)
