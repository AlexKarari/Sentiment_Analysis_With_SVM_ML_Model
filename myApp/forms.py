from django import forms

class sentimentForm(forms.Form):
    your_sentiment = forms.CharField(widget=forms.Textarea)
    