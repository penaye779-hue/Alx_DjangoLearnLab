from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = "__all__"

    def clean_title(self):
        title = self.cleaned_data.get("title")
        if "<script>" in title.lower():
            raise forms.ValidationError("Invalid input detected.")
        return title
from django import forms

class ExampleForm(forms.Form):
    title = forms.CharField(max_length=200)
    description = forms.CharField(widget=forms.Textarea, required=False)
