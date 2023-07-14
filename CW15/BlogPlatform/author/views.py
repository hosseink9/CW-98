from django.shortcuts import render, get_object_or_404
from .models import Author

def all_author(request):
    authors = Author.objects.all()
    context = {"authors": authors}
    return render(request, "author.html", context)


def author_details(request, pk):
    author = get_object_or_404(Author, pk=pk)
    
    return render(request, "author_details.html", {"author": author})

