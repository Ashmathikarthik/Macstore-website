from django import forms
from .models import SupportMessage

class ContactForm(forms.ModelForm):
    class Meta:
        model = SupportMessage
        fields = ['name', 'email', 'phone', 'subject', 'message']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Your Full Name',
                'required': 'required'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Your Email Address',
                'required': 'required'
            }),
            'phone': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Your Phone Number'
            }),
            'subject': forms.Select(attrs={
                'class': 'form-control',
                'required': 'required'
            }),
            'message': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Please describe your issue or question in detail...',
                'rows': 5,
                'required': 'required'
            }),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['subject'].choices = [
            ('', 'Select a subject'),
            ('order', 'Order Inquiry'),
            ('technical', 'Technical Support'),
            ('product', 'Product Information'),
            ('return', 'Returns & Refunds'),
            ('complaint', 'Complaint'),
            ('other', 'Other')
        ]
