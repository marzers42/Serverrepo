from django import forms
from .models import *

class ServidorVirtualForm(forms.ModelForm):

    class Meta:
        model = ServidorVirtual
        fields = "__all__"

        widgets = {
            'Descripcion': forms.Textarea(attrs={'class': 'form-control'}),
        }