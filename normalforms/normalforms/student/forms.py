from django import forms

class Registration(forms.Form):
    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField()
    city = forms.CharField()

class Login(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput())

class Exampleform(forms.Form):
    # basic field
    name = forms.CharField()
    email = forms.EmailField()
    pincode = forms.IntegerField()

    # additional field types
    age = forms.FloatField()
    dob = forms.DateField()
    appointement_time = forms.TimeField()
    appointement_datetime = forms.DateTimeField()
    is_subscribed = forms.BooleanField()
    agree_terms =  forms.NullBooleanField()

    # choice fields 
    gender = forms.ChoiceField(choices=[('M','Male'), ('F', "Female"), ('O', "Other")])

    '''other fields are -
    imagefield, filefield, urlfield, regexfield, slugfield, genericipaddressfield
    '''