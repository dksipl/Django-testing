from django import forms
from django.forms import ModelForm
from app1.models import IrisModel

class IrisForm(forms.ModelForm):
    
    class Meta:
        
        model = IrisModel
        fields = ['sepal_length', 'sepal_width',
                  'petal_length', 'petal_width']