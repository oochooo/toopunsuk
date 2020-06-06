from django import forms
from .models import Cabinet, Update

class CabinetForm(forms.ModelForm):
    
    class Meta:
        model = Cabinet
        fields = [
            'name_text', 'image', 'lat', 'lng'
        ]

        widgets = {
            'name_text': forms.Textarea(attrs={'rows': 10, 'cols': 30})
        }

        labels = {
            'name_text' : 'Address'
        }

class UpdateForm(forms.ModelForm):
    
    class Meta:
        model = Update
        fields = [
            'cabinet', 'pub_date',
            'comment_text', 'need_refill', 'image_update'
        ]
        widgets = {
          'comment_text': forms.Textarea(attrs={'rows':4, 'cols':30}),
        }