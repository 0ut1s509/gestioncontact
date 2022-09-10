from django import forms
from .models import Contact
from django.core.exceptions import ValidationError
class ContactForm(forms.ModelForm):
    class Meta:
        model=Contact
        fields='__all__'

    def clean(self):
        cleaned_data=super().clean()

        phone=cleaned_data.get('phone_number')
        name=cleaned_data.get('fullname')
        email=cleaned_data.get('email')

        if Contact.objects.filter(fullname = name):
            self.add_error('fullname','this name already exist')

        if Contact.objects.filter(phone_number = phone):
            self.add_error('phone_number', 'This phone number already exist')

        if Contact.objects.filter(email = email):
            self.add_error('email', 'This email already exist')
        
