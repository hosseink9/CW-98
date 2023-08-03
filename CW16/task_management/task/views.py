from django.shortcuts import render, get_object_or_404
from .models import Task
from epic_quest.models import Tag

def all_task(request):
    tasks = Task.objects.all()
    context = {"tasks": tasks}
    return render(request, "home.html", context)


def task_details(request, pk):
    task = get_object_or_404(Task, pk=pk)
    recently_viewed_tasks = None

    if 'recently_viewed' in request.session:
        if pk in request.session['recently_viewed']:
            request.session['recently_viewed'].remove(pk)

        tasks = Task.objects.filter(pk__in = request.session['recently_viewed'])
        recently_viewed_tasks = sorted(tasks,key = lambda x: request.session['recently_viewed'].index(x.pk))
        request.session['recently_viewed'].insert(0, pk)
        if len(request.session['recently_viewed']) > 5:
            request.session['recently_viewed'].pop()

    else:
        request.session['recently_viewed'] = [pk]
    
    request.session.modified = True

    return render(request, "task_details.html", {"task": task,'recently_viewed_tasks':recently_viewed_tasks})
