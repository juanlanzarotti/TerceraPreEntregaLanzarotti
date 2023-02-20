from django.contrib import admin
from .models import Ingredients, Equipment, Comments

# Register your models here.
admin.site.register(Ingredients)
admin.site.register(Equipment)
admin.site.register(Comments)