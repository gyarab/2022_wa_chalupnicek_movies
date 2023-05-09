from django import forms
from django.core.validators import MaxValueValidator, MinValueValidator

class CommentForm(forms.Form):
    author = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Pepa z Depa"})
    )
    text = forms.CharField(
        required=False,
        widget=forms.Textarea(attrs={"rows": 5, "class": "form-control"})
    )
    rating = forms.IntegerField(
        required=False,
        widget=forms.NumberInput(attrs={"class": "form-control"}),
        validators=[
            MaxValueValidator(100),
            MinValueValidator(1)
        ]
    )
