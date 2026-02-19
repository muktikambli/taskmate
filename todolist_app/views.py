from django.http import HttpResponse, request
from django.shortcuts import redirect, render
from django.template import context
from todolist_app.models import TaskList    
from todolist_app.forms import TaskForm
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='login')
def todolist(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save(commit=False).manager = request.user
            form.save()
            messages.success(request, "New Task Added Successfully!")
            return redirect('todolist')
    else:
        form = TaskForm()
    
    tasks = TaskList.objects.filter(manager=request.user).order_by('-id')
    paginator = Paginator(tasks, 10)
    page = request.GET.get('page')
    tasks = paginator.get_page(page)
    return render(request, 'todolist.html', {
        'welcome_text': "Welcome to TodoList App!", 
        'all_tasks': tasks,
        'form': form
    })   

@login_required(login_url='login')
def delete_task(request, task_id):
    task = TaskList.objects.get(pk=task_id)
    if task.manager == request.user:
        task.delete()
        messages.success(request, "Task Deleted Successfully!")
        return redirect('todolist')
    else:
        messages.error(request, "Access Denied")
        return redirect('todolist')
  

@login_required(login_url='login')
def update_task(request, task_id):
    if request.method == "POST":    
        task = TaskList.objects.get(pk=task_id)
        form = TaskForm(request.POST or None, instance=task)
        if form.is_valid():
            form.save()
            messages.success(request, "Task Updated Successfully!")
            return redirect('todolist')
        else:
            return render(request, 'update.html', {'task': task})
    else:
        task = TaskList.objects.get(pk=task_id)
        return render(request, 'update.html', {'task': task})


@login_required(login_url='login')
def complete_task(request, task_id):
    task = TaskList.objects.get(pk=task_id)
    if task.manager == request.user:
        task.done = True
        task.save()
        messages.success(request, "Task Completed Successfully!")
        return redirect('todolist')
    else:
        messages.error(request, "Access Denied")
        return redirect('todolist')

@login_required(login_url='login')
def pending_task(request, task_id):
    task = TaskList.objects.get(pk=task_id)
    task.done = False
    task.save()
    #messages.success(request, "Task Pending Successfully!")
    return redirect('todolist')


def index(request):
    context = {
        'indextext': "Home Page"
    }
    return render(request, 'index.html', context) 


def contact(request):
    context = {
        'contact_text': "Contact Us."
    }
    return render(request, 'contact.html', context)  


def about(request):
    context = {
        'about_text': "About Us."
    }
    return render(request, 'about.html', context)  
