from django import forms
from django.contrib.auth.models import User
from .models import Image

class ImageForm(forms.ModelForm):
    class Meta():
        model = Image
        fields = "__all__"

