from . import views
from django.urls import path

app_name = "cliente"

urlpatterns = [
    path("", views.index, name="index"),
    path("list/", views.cliente_list, name="list"),
    path("form/", views.cliente_create, name="form"),
    path("detail/<int:pk>", views.cliente_detail, name="detail"),
    path("update/<int:pk>", views.cliente_update, name="update"),
    path("delete/<int:pk>", views.cliente_delete, name="delete"),
]
