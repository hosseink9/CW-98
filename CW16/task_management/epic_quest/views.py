from django.shortcuts import render, get_object_or_404,redirect
from django.db.models import Q
from .models import Category, Tag
from task.models import Task
from itertools import chain
from django.core.paginator import Paginator

def home(request):
        if request.method == "POST":
                title = request.POST['title']
                description = request.POST['description']
                due_date = request.POST['due_date']
                category_name = request.POST['category']
                # category = Category.objects.all()
                status_fields = request.POST['status_fields']
                tag_name = request.POST['tag']
                # tag = Tag.objects.all()
                add_task=Task(name=title,description=description,due_date=due_date,category=category_name,status_fields=status_fields,tag=tag_name)
                add_task.save()
                # print(title,description,due_date,category,status_fields,
                return redirect("all_category")
        elif request.method == "GET":
                tasks = Task.objects.all()
                pagintion=Paginator(Task.objects.all(), 2)
                page = request.GET.get('page')
                task_list=pagintion.get_page(page)
                categorys=Category.objects.all()
                status={item[0]:item[1] for item in Task.status_choice}
                tags=Tag.objects.all()
        return render(request, "home.html", {"tasks": tasks,'task_list':task_list,'categorys':categorys,'status':status,'tags':tags})

def view_all(request):
        tasks = Task.objects.order_by('due_date')
        pagintion=Paginator(Task.objects.order_by('due_date'), 2)
        page = request.GET.get('page')
        task_list=pagintion.get_page(page)
        return render(request, "view_all.html", {"tasks": tasks,'task_list':task_list})
        
      

def search(request):
    return render(request,'search.html')

def all_category(request):
        if request.method == "POST":
                title = request.POST['title']
                description = request.POST['description']
                add_category=Category(name=title,description=description)
                add_category.save()
                return redirect("all_category")
        elif request.method == "GET":
                categorys = Category.objects.all()
                tasks = Task.objects.all()
                return render(request, "category.html",{"categorys": categorys,"tasks": tasks})

def category_details(request, pk):
    category = get_object_or_404(Category, pk=pk)
    tasks=Task.objects.filter(category=category)
    return render(request, "category_detalis.html", {"category": category,"tasks":tasks})

def search_details(request):
        if request.method == "GET":
            searched = request.GET.get('searched')
            tasks = Task.objects.filter(
            Q(title__contains=searched) | Q(tag__name__contains=searched)).distinct()
            return render(request, "search_details.html", {'searched':searched, 'tasks': tasks})
        else:
             return render(request, "search_details.html", {})
        