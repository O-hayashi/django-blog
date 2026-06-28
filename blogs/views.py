from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from .models import Blog, Category, Comment
from django.db.models import Q

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


def blogs(request, slug):
  single_blog = get_object_or_404(Blog, slug = slug, status = 'Published')
  if request.method == 'POST':
    comment = Comment()
    comment.user = request.user
    comment.blog = single_blog
    comment.comment = request.POST['comment']
    comment.save()
    return HttpResponseRedirect(request.path_info)
  comments = Comment.objects.filter(blog=single_blog)
  comments_count = Comment.objects.filter(blog = single_blog).count()
  context = {
    'single_blog': single_blog,
    'comments': comments,
    'comments_count': comments_count,
  }
  return render(request, 'blogs.html', context)

def search(request):
  keyword = request.GET.get("keyword")
  blogs = Blog.objects.filter(
    Q(title__icontains=keyword) |
    Q(short_description__icontains = keyword) | 
    Q(blog_body__icontains = keyword)
  )
  context = {
    'blogs': blogs,
    'keyword':keyword,
  }
  return render(request, 'search.html', context)

