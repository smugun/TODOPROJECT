from django.shortcuts import render, redirect
from .forms import TaskForm, UpdateTaskForm
from .models import Task


# Create your views here.
def index(request):
    todos = Task.objects.all()
    count_todos = todos.count()

    completed_todo = Task.objects.filter(complete=True)
    count_completed_todo = completed_todo.count()
    count_uncompleted_todo = count_todos - count_completed_todo

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = TaskForm()
    context = {
        'todos': todos,
        'form': form,
        'count_todos': count_todos,
        'count_completed_todo': count_completed_todo,
        'count_uncompleted_todo': count_uncompleted_todo,
    }
    return render(request, 'todo/index.html', context)


def update(request, pk):
    todo = Task.objects.get(id=pk)
    if request.method == 'POST':
        form = UpdateTaskForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            return redirect('/')

    else:
        form = UpdateTaskForm(instance=todo)

    context = {
         'form': form,
    }
    return render(request, 'todo/update.html', context)


def delete(request, pk):
    todo = Task.objects.get(id=pk)
    if request.method == 'POST':
        todo.delete()
        return redirect('/')

    context = {
        'todo': todo,
    }
    return render(request, 'todo/delete.html', context)
