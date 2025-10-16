from datetime import datetime
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from .models import Tasks
from django.views.decorators.http import require_POST

# Create your views here.
def index(request):
    tasks = Tasks.objects.order_by("-created_at")
    task_context = {"tasks": tasks}
    return render(request, "todo/index.html", task_context)

@require_POST
def toggle(request, task_id):
    task_action = get_object_or_404(Tasks, pk=task_id)
    task_action.is_done = not task_action.is_done
    task_action.completed_at = datetime.now() if task_action.is_done else None
    task_action.save(update_fields=["is_done", "completed_at"])

    return redirect("todo:index")

def add(request):
    return render(request, "todo/add.html")

