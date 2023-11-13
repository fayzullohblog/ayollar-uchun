from django import forms
from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.core.exceptions import ValidationError

from .models import User, Job
from .forms import UserCreationForm, UserChangeForm, UserPasswordChageForm


class UserAdmin(BaseUserAdmin):
    change_password_form = UserPasswordChageForm
    form = UserChangeForm
    add_form = UserCreationForm

    list_display = [
        'first_name',
        'last_name',
        "phone_number",
        'is_superuser',
        'is_active',
        'email',
    ]
    list_filter = []
    fieldsets = [
        (None, {"fields": [
            "password",
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
        ]}),
    ]
    add_fieldsets = [
        (
            None,
            {
                "classes": ["wide"],
                "fields": [
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
                ],
            },
        ),
    ]
    readonly_fields = ('phone_number',)
    search_fields = ["phone_number", 'first_name', 'last_name']
    ordering = ["id"]
    filter_horizontal = []


admin.site.register(User, UserAdmin)
admin.site.register(Job)
