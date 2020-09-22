from .models import Docker
from django.forms import ModelForm
from django.contrib import admin


class dockerform(ModelForm):
    class Meta:
        model = Docker
        fields = ['ContainerName','image','command','user',]
