from django import forms
from notes.models import Note


# Create your forms here


class NotesForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = '__all__'
