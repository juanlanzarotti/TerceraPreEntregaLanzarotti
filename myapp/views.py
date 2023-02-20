from django.http import HttpResponse
from .models import Ingredients, Equipment, Comments
from django.shortcuts import render, redirect
from .forms import CreateNewIngredient, CreateNewEquipment, CreateNewComment

# Create your views here.
def index(request):
    title = 'Coder-Beer'
    return render(request, 'index.html', {
        'title': title
    })

def create_new_ingredient(request):
    if request.method == 'GET':
        return render(request, 'create_new_ingredient.html', {
            'form': CreateNewIngredient()
        })
    else:
        ingredient = Ingredients.objects.create(name=request.POST['name'], description=request.POST['description'])
        return render(request, 'create_new_ingredient.html', {
            'form': CreateNewIngredient()
        })

   
def create_new_equipment(request):
    if request.method == 'GET':
        return render(request, 'create_new_equipment.html', {
            'form': CreateNewEquipment()
        })
    else:
        equipment = Equipment.objects.create(name=request.POST['name'], description=request.POST['description'])
        print(equipment)
        return render(request, 'create_new_equipment.html', {
            'form': CreateNewEquipment()
        })

            
def create_new_comment(request):
    if request.method == 'GET':
        return render(request, 'create_new_comment.html', {
            'form': CreateNewComment()
        })
    else:
        comment = Comments.objects.create(description=request.POST['description'])
        return render(request, 'create_new_comment.html', {
            'form': CreateNewComment()
        })
    
def search_ingredients(request):
    query = request.GET.get('q')
    if query:
        resultados = Ingredients.objects.filter(name__icontains=query)
    else:
        resultados = []
    return render(request, 'search_ingredients.html', {"Ingredients": resultados})
