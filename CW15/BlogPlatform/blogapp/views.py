from django.shortcuts import render, get_object_or_404
from .models import Post, Category

def home(request):
    return render(request,'home.html')

def all_post(request):
    posts = Post.objects.all()
    context = {"posts": posts}
    return render(request, "post.html", context)

def post_details(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, "post_details.html", {"post": post})


def all_category(request):
    categorys = Category.objects.all()
    context = {"categorys": categorys}
    return render(request, "category.html", context)

def category_details(request, pk):
    category = get_object_or_404(Category, pk=pk)
    return render(request, "category_detalis.html", {"category": category})
