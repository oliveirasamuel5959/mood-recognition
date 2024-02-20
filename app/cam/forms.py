from django import forms

class InputImageForm(forms.Form):
    class Meta:
        fields = ('img')
        
    image = forms.ImageField(widget=forms.FileInput(attrs={
        'class': 'py-4 px-6 ',
    }))