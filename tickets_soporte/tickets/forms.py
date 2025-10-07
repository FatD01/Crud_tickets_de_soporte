# tickets/forms.py
from django import forms
from .models import Categoria, Ticket

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = '__all__'

class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        # Excluimos id y fecha_creacion, que son automáticos
        fields = ['titulo', 'descripcion', 'estado', 'categoria', 'adjunto']