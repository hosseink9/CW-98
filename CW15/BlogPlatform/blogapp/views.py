from django.shortcuts import render, get_object_or_404
from .models import Post, Category
from author.models import Author

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
    context = {"category": categorys}
    return render(request, "category.html", context)

def all_author(request):
    authors = Author.objects.all()
    context = {"author": authors}
    return render(request, "author.html", context)