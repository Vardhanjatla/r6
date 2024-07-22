from django import forms
from .models import Server, Folder

class SyncForm(forms.Form): 
    source_server = forms.ModelChoiceField(queryset=Server.objects.all())
    source_folder = forms.ModelChoiceField(queryset=Folder.objects.all())
    destination_server = forms.ModelChoiceField(queryset=Server.objects.all())
    destination_folder = forms.ModelChoiceField(queryset=Folder.objects.all())