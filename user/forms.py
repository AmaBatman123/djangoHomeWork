from django import forms
from django.contrib.auth.forms import User

class RegisterForm(forms.ModelForm):
    password_confirm = forms.CharField(
        required=True
    )
    class Meta:
        model = User
        fields = ['username', 'password', 'password_confirm']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password_confirm = cleaned_data.get("password_confirm")

        if (password and password_confirm) and (password != password_confirm):
            raise forms.ValidationError("Passwords must match")
        return cleaned_data