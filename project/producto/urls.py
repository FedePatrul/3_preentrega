from . import views
from django.urls import path

app_name = "producto"

urlpatterns = [
    path("", views.index, name="index"),
    path("list/", views.producto_list, name="list"),
    path("form/", views.producto_create, name="form"),
    path("detail/<int:pk>", views.producto_detail, name="detail"),
    path("update/<int:pk>", views.producto_update, name="update"),
    path("delete/<int:pk>", views.producto_delete, name="delete"),
]
