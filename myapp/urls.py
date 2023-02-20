from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('search_ingredients/', views.search_ingredients, name='search_ingredients'),
    path('create_new_ingredient/', views.create_new_ingredient, name='Ingredientes'),
    path('create_new_equipment/', views.create_new_equipment, name='Equipamiento'),
    path('create_new_comment', views.create_new_comment, name='Comentarios'),
]