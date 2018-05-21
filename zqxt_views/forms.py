from django import forms
from models import CureData

class CureDataImageForm(forms.ModelForm):

    class Meta:
        model = CureData
        fields = '__all__'  # ['name', 'create_at',  ...] 

