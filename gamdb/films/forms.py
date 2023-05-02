from django import forms

class CommentForm(forms.Form):
    author = forms.CharField(required=False)
    text = forms.CharField(required=False, widget=forms.Textarea(attrs={"rows": 5}))
    rating = forms.IntegerField(required=False)
