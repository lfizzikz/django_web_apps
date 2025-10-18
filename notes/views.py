from datetime import datetime
from django.shortcuts import get_object_or_404, render, redirect
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
        note_id = request.GET.get("note")
        if note_id:
            note_body_action = get_object_or_404(Notes, pk=note_id)
            note_body = request.POST.get("note_body", "")
            note_body_action.body = note_body 
            note_body_action.updated_at = datetime.now()
            note_body_action.save(update_fields=["body", "updated_at"])

            return redirect("notes:index")
