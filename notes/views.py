from datetime import datetime
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from .models import Notes

# Create your views here.
def index(request):
    note_list = Notes.objects.order_by("-updated_at", "-created_at")
    note_id = request.GET.get("note")

    if note_id:
        selected_note = get_object_or_404(note_list, pk=note_id)
    else:
        selected_note = note_list.first() if note_list.exists() else None

    context = {
        "note_list": note_list,
        "selected_note": selected_note
    }

    return render(request, "notes/index.html", context)

def save(request):
    if request.method == "POST":
        action = request.POST.get("action", "save")
        note_id = request.GET.get("note")
        if not note_id:
            return redirect("notes:index")
        note_action = get_object_or_404(Notes, pk=note_id)
        if action == "delete":
            note_action.delete()
            return redirect("notes:index")
        note_body = request.POST.get("note_body", "")
        note_title = request.POST.get("note_title", "")
        note_action.body = note_body 
        note_action.title = note_title
        note_action.updated_at = datetime.now()
        note_action.save(update_fields=["body", "updated_at", "title"])

        return redirect("notes:index")


def new_note(request):
    if request.method == "POST":
        new_note = Notes.objects.create(title="", body="", created_at=datetime.now())

        return redirect(f"{reverse('notes:index')}?note={new_note.pk}")
