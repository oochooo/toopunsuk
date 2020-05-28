from django import forms
from .models import Cabinet, Update

class CabinetForm(forms.ModelForm):
    
    class Meta:
        model = Cabinet
        fields = [
            'name_text', 'image', 'lat', 'lng'
        ]

class UpdateForm(forms.ModelForm):
    
    class Meta:
        model = Update
        fields = [
            'cabinet', 'pub_date',
            'comment_text', 'need_refill', 'image_update'
        ]