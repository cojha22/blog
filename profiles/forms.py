from django import forms
from profiles.models import UersProfile

class ProfileForm(forms.ModelForm):
    class Meta:
        model = UersProfile
        fields =['firstname','lastname','profile_image','contact','address']

        widgets ={
            "firstname": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Please provide Title for Post",
                }
            ),
            "lastname": forms.Textarea(
                attrs={
                    "class": "forms-control",
                }
            ),
            "profile_image": forms.FileInput(attrs={"class": "form-control",
                                                    }
                                             ),
             "contact": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Please provide Title for Post",
                }
            ),
             "address": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Please provide Title for Post",
                }
            ),
        }