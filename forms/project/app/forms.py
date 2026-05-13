# A standard Form class maps directly to HTML form fields.  Here is how we can structure a basic feedback form

from django import forms

class FeedbackForm(forms.Form):
    name = forms.CharField(max_length=100, label='Your Name')
    email = forms.EmailField(label='Your Email')
    subject = forms.CharField(max_length=200, label='Subject')
    message = forms.CharField(widget=forms.Textarea, label='Your Feedback')

    # Widgets: These handle the presentation—the Textarea widget tells Django to render a multi-line box instead of a single-line input.