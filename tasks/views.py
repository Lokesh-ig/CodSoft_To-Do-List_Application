from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Task
from .forms import TaskForm

def task_list(request):
    search_query = request.GET.get('search', '').strip()
    status_filter = request.GET.get('status', '').strip()
    priority_filter = request.GET.get('priority', '').strip()
    category_filter = request.GET.get('category', '').strip()

    tasks = Task.objects.all()

    if search_query:
        tasks = tasks.filter(
            Q(title__icontains=search_query) | Q(description__icontains=search_query)
        )

    if status_filter:
        if status_filter.lower() == 'all':
            pass  # Show all tasks including completed
        else:
            normalized_status = status_filter.replace('-', ' ').replace('_', ' ')
            tasks = tasks.filter(status__iexact=normalized_status)
    else:
        # Default home view: exclude completed tasks so they only appear in the Completed section
        tasks = tasks.exclude(status__iexact='Completed')

    if priority_filter:
        tasks = tasks.filter(priority__iexact=priority_filter)

    if category_filter:
        tasks = tasks.filter(category__iexact=category_filter)

    total_tasks = Task.objects.count()
    completed_tasks = Task.objects.filter(status='Completed').count()
    pending_tasks = Task.objects.filter(status='Pending').count()
    in_progress_tasks = Task.objects.filter(status='In Progress').count()

    form = TaskForm()

    context = {
        'tasks': tasks,
        'form': form,
        'search_query': search_query,
        'status_filter': status_filter,
        'priority_filter': priority_filter,
        'category_filter': category_filter,
        'total_tasks': total_tasks,
        'completed_tasks': completed_tasks,
        'pending_tasks': pending_tasks,
        'in_progress_tasks': in_progress_tasks,
    }
    return render(request, 'tasks/task_list.html', context)

def task_create(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Task created successfully!')
        else:
            messages.error(request, 'Failed to create task. Please check your inputs.')
    return redirect('task_list')

def task_update(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            messages.success(request, 'Task updated successfully!')
            return redirect('task_list')
    else:
        form = TaskForm(instance=task)
    return render(request, 'tasks/task_form.html', {'form': form, 'task': task})

def task_delete(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        task.delete()
        messages.success(request, 'Task deleted successfully!')
        return redirect('task_list')
    return render(request, 'tasks/task_confirm_delete.html', {'task': task})

def task_toggle(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if task.status == 'Completed':
        task.status = 'Pending'
    else:
        task.status = 'Completed'
    task.save()
    messages.info(request, f'Task status updated to "{task.status}"!')
    return redirect('task_list')
