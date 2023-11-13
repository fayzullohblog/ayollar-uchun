from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.core.exceptions import ValidationError

from .models import User


class UserCreationForm(forms.ModelForm):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""

    password1 = forms.CharField(label="Password", widget=forms.PasswordInput)
    password2 = forms.CharField(
        label="Password confirmation", widget=forms.PasswordInput
    )

    class Meta:
        model = User
        fields = [
            "phone_number",
            'first_name',
            'last_name',
            'gender',
            'is_superuser',
            'is_active',
            'birth_day',
            'email',
            'country',
            'region',
            'postcode',
            'address',
            'instagram',
            'imkon_uz',
            'linkedin',
            'workplace',
            'job',
            'about',
            "password",
        ]

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    disabled password hash display field.
    """
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = [
            "phone_number",
            'first_name',
            'last_name',
            'gender',
            'is_superuser',
            'is_active',
            'birth_day',
            'email',
            'country',
            'region',
            'postcode',
            'address',
            'instagram',
            'imkon_uz',
            'linkedin',
            'workplace',
            'job',
            'about',
            "password",
        ]

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        print(super())
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user


class UserPasswordChageForm(forms.ModelForm):
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput)
    password2 = forms.CharField(
        label="Password confirmation", widget=forms.PasswordInput
    )

    class Meta:
        model = User
        fields = ['phone_number', 'password1', 'password2']

    def save(self, commit=True):
        user = super(UserChangeForm, self).save(commit=False)
        cleaned_data = self.cleaned_data
        new_pass = cleaned_data['password1']
        user.set_password(new_pass)
        # here sending email can be initiated
        if commit:
            user.save()
        return user
