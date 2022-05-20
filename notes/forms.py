from django import forms
from .models import Note


class NoteModelForm(forms.ModelForm):

    extra_field = forms.CharField()

    def save(self, commit=True):
        extra_field = self.cleaned_data.get('extra_field', None)
        # ...do something with extra_field here...
        return super(NoteModelForm, self).save(commit=commit)

    class Meta:
        model = Note
