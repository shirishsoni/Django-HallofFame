from .models import Video
from django import forms


# Model form
class VideoForm(forms.ModelForm):
    class Meta:
        model = Video
        fields = ['url']
        labels = {'url':'YouTube URL'}

# Simple Form
class SearchForm(forms.Form):
    search_term = forms.CharField(max_length=255, label='Search for Video:')
