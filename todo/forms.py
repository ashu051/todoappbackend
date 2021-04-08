from django import forms
from .models import Todo
class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields=['name']
        widgets={
            'name':forms.TextInput(attrs={'class':'form-control'}),
        }
        labels={'name':'Task--Data'}