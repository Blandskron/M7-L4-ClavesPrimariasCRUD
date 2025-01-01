from django import forms
from .models import ChildModel

class ChildModelForm(forms.ModelForm):
    class Meta:
        model = ChildModel
        fields = ['parent', 'description']