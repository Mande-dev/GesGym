from django import forms
from .models import Member


class MemberCreationForm(forms.ModelForm):
    """
    Formulaire de création / modification membre
    """

    class Meta:
        model = Member
        fields = [
            "first_name",
            "last_name",
            "phone",
            "email",
            "address",
            "photo",
        ]

        widgets = {
            "first_name": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Prénom"
            }),
            "last_name": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Nom"
            }),
            "phone": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Téléphone"
            }),
            "email": forms.EmailInput(attrs={
                "class": "form-control",
                "placeholder": "Email"
            }),
            "address": forms.Textarea(attrs={
                "class": "form-control",
                "rows": 2,
                "placeholder": "Adresse"
            }),
            "photo": forms.FileInput(attrs={
                "class": "form-control"
            }),
        }