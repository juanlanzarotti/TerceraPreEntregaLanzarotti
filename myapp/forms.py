from django import forms


class CreateNewIngredient(forms.Form):
    name = forms.CharField(
        label='',
        max_length=200,
        widget=forms.TextInput(attrs={
            'placeholder': 'Nombre del ingrediente',
        })
    )
    description = forms.CharField(
        label='',
        widget=forms.Textarea(attrs={
            'placeholder': 'Descripcion del ingrediente',
        })
    )

class CreateNewEquipment(forms.Form):
    name = forms.CharField(
        label='',
        max_length=200,
        widget=forms.TextInput(attrs={
            'placeholder': 'Nombre del equipamiento',
        })
    )
    description = forms.CharField(
        label='',
        widget=forms.Textarea(attrs={
            'placeholder': 'Descripcion del equipamiento',
        })
    )

class CreateNewComment(forms.Form):
    description = forms.CharField(label='',widget=forms.Textarea(attrs={'placeholder': 'Comentario del usuario',}))
