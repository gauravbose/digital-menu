from django import forms

class NameForm(forms.Form):
    content = forms.CharField(label='content', max_length=100)
