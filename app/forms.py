from django import forms


from app.models import *
class NameForm(forms.ModelForm):
    class Meta:
        model= Topic
        fields='__all__'
