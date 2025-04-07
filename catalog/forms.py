from django import forms
from .models import Book, Category


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'category']
        widgets = {
            'title': forms.TextInput(attrs={'required': True}),
            'author': forms.TextInput(attrs={'required': True}),
        }

    def clean_title(self):
        title = self.cleaned_data['title']
        if len(title) < 3:
            raise forms.ValidationError("Название должно быть длиннее 3 символов")
        return title


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']
