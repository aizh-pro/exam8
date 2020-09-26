from django import forms
from django.core.exceptions import ValidationError

from webapp.models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description','category', 'picture']

    def clean(self):
        cleaned_data = super().clean()
        errors = []
        description = cleaned_data.get('description')
        name = cleaned_data.get('name')
        category = cleaned_data.get('category')
        picture = cleaned_data.get('picture')
        if description and name and description == name:
            errors.append(ValidationError("Text  should not duplicate it's name!"))
        if errors:
            raise ValidationError(errors)
        return cleaned_data
