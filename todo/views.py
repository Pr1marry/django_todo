from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods

from .models import Todolist


def index(request):
    todos = Todolist.objects.all()
    return render(request, 'todoapp/index.html', {'todo_list': todos, 'title': 'Todoska'})


@require_http_methods(['POST'])
def add(request):
    title = request.POST['title']
    todo = Todolist(title=title)
    todo.save()
    return redirect('index')


def update(request, todo_id):
    todo = Todolist.objects.get(id=todo_id)
    todo.is_complete = not todo.is_complete
    todo.save()
    return redirect('index')


def delete(request, todo_id):
    todo = Todolist.objects.get(id=todo_id)
    todo.delete()
    return redirect('index')
