from . import views
from django.urls import path

app_name = "empleado"

urlpatterns = [
    path("", views.index, name="index"),
    path("list/", views.empleado_list, name="list"),
    path("form/", views.empleado_create, name="form"),
    path("detail/<int:pk>", views.empleado_detail, name="detail"),
    path("update/<int:pk>", views.empleado_update, name="update"),
    path("delete/<int:pk>", views.empleado_delete, name="delete"),
]
