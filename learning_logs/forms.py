from django import forms
from django_summernote.widgets import SummernoteWidget

from .models import Topic, Entry

class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['text']
        labels = {'text': ''}


class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['text']
        widgets = {
            'text': SummernoteWidget(),
        }
        labels = {'text': ''}
