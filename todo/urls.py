from django.urls import path
from . import views


app_name = "todo"
urlpatterns = [
    path("", views.index, name="index"),
    # path("tasks/add/", views.add, name="add"),
    path("tasks/<int:task_id>/toggle/", views.toggle, name="toggle"),
    # path("tasks/<int:task_id>/delete/", views.delete, name="delete"),
]

