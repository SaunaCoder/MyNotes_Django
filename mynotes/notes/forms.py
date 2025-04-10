from django import forms
from .models import *

class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ('title', 'text')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'text': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
        }