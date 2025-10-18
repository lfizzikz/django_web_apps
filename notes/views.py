from django.shortcuts import get_object_or_404, render
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
