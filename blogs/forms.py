from ckeditor.widgets import CKEditorWidget
from django import forms
from django.contrib import admin

from . models import Articls

class NewArtForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorWidget())
    class Meta:
        model = Articls
        fields = ['title','content','author']

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('user', None)
        super(NewArtForm, self).__init__(*args, **kwargs)

    def save(self, commit=True, *args, **kwargs):
        instance = super().save(commit=False)
        instance.author = self.request
        if commit:
            instance.save()
        return instance

