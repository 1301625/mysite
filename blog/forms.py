from django import forms
from .models import Post
from .widgets import TuiEditorWidget,CounterTextInput

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'text', 'photo', 'tags']
        widgets = {
            'title': CounterTextInput,
            'text' : TuiEditorWidget,
        }