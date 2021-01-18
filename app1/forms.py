from django import forms
from .models import Touroku

class KenkoRecord(forms.ModelForm):
    class Meta:
        model = Touroku
        fields = ['name','text']

class IdKensaku(forms.Form):
    id = forms.CharField(label = "ID")