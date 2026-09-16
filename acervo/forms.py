from django import forms

from .models import Livro


class LivroForm(forms.ModelForm):
    class Meta:
        model = Livro
        fields = ("titulo", "autor", "ano", "tipo", "categoria")
        widgets = {
            "titulo": forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'Título do livro'}
            ),
            "autor": forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'Nome do autor'}
            ),
            'ano': forms.NumberInput( 
            attrs={
                'class': 'form-control',
                'placeholder': 'Ex: 2026',
                'min': '1440',
            }),
            "tipo": forms.Select(
                attrs={"class":"form-control"}
            ),
            'categoria': forms.Select(
                attrs={'class': 'form-control'}
            ),
        }
