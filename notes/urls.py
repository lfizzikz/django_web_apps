from django.urls import path
from . import views


app_name = "notes"
urlpatterns = [
    path("", views.index, name="index"),
    path("/save", views.save, name="save"),
    path("/new", views.new_note, name="new_note"),
]
