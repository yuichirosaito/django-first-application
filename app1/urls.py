from django.urls import path
from . import views

urlpatterns = [
    path('', views.index,name="index"),
    path('create', views.create,name="create"),
    path('edit/<int:number>', views.edit,name="edit"),
    path('delete/<int:number>', views.delete,name="delete"),
]