from django import forms
from django.core.validators import validate_email
import phonenumbers

def validate_phone_number(value):
    z = phonenumbers.parse(value, "GB")
    try:
        if phonenumbers.is_valid_number(z):
            return True
    except (ValueError, TypeError, phonenumbers.NumberParseException):
        if not phonenumbers.is_valid_number(z):
            raise forms.ValidationError(
                ('%(value) is not a valid phone number'),
                params={'value': value},
            )

def should_be_empty(value):
    if value:
        raise forms.ValidationError('Field is not empty')    


class ContactForm(forms.Form):
    first_name = forms.CharField(max_length=80)
    last_name = forms.CharField(max_length=80)
    email = forms.EmailField(label='Email Address', validators=[validate_email])
    phone = forms.CharField(validators=[validate_phone_number])
    message = forms.CharField(max_length='5000', widget=forms.Textarea)
    trizzap = forms.CharField(required=False, widget=forms.HiddenInput, label='leave empty', validators=[should_be_empty])


class Newsletter(forms.Form):
    email = forms.EmailField(label='Email Address', validators=[validate_email])
    trappa = forms.CharField(required=False, widget=forms.HiddenInput, label='leave empty', validators=[should_be_empty])