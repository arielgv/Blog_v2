from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
        }

class PostFilterForm(forms.Form):
    FILTER_CHOICES = (
        ('newest', 'Newest'),
        ('oldest', 'Oldest'),
        ('most_liked', 'Most Liked'),
    )
    filter_by = forms.ChoiceField(choices=FILTER_CHOICES, required=False)
    search = forms.CharField(max_length=100, required=False)