from django import forms

from .models import UrlService


class UrlShortForm(forms.ModelForm):
    class Meta:
        model = UrlService
        fields = ('url_all',)

