from django.db import models

# Create your models here.
class Ingredients(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return f'Nombre: {self.name} - Descripcion: {self.description}'

class Equipment(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return f'Nombre: {self.name} - Descripcion: {self.description}'
    
class Comments(models.Model):
    description = models.TextField()

    def __str__(self):
        return f'Descripcion: {self.description}'

