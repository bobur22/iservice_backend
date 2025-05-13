from django import forms
from django.contrib.auth import get_user_model
from iservice.models import Location
from django.utils.translation import gettext_lazy as _

User = get_user_model()


class UserForm(forms.ModelForm):
    full_name = forms.CharField(required=True, widget=forms.TextInput(attrs={
        'name': "full_name",
        'placeholder': 'Full Name',
        "class": "form-control py-3 ps-4 pe-4 font_f_n color_g shadow-sm bg-body",
        "style": "border-radius: 14px; border: 1px solid #D8E0F0 !important;",
    }))

    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={
        'name': "emp_email",
        'placeholder': 'Email',
        "class": "form-control py-3 ps-4 pe-4 font_f_n color_g shadow-sm bg-body",
        "style": "border-radius: 14px; border: 1px solid #D8E0F0 !important;",
    }))

    birthdate = forms.DateField(
        widget=forms.DateInput(attrs={
            'type': 'date',  # 👈 this enables the date picker
            'name': 'birthdate',
            'placeholder': 'Birthdate',
            "class": "form-control py-3 ps-4 pe-4 font_f_n color_g shadow-sm bg-body",
            "style": "border-radius: 14px; border: 1px solid #D8E0F0 !important;",
        }, format='%Y-%m-%d'),
        required=True,
    )

    position = forms.CharField(required=True, widget=forms.TextInput(attrs={
        'name': "position",
        'placeholder': 'Position',
        "class": "form-control py-3 ps-4 pe-4 font_f_n color_g shadow-sm bg-body",
        "style": "border-radius: 14px; border: 1px solid #D8E0F0 !important;",
    }))

    p_number = forms.CharField(required=True, widget=forms.TextInput(attrs={
        'name': "emp_number",
        'placeholder': 'Phone Number',
        "class": "form-control py-3 ps-4 pe-4 font_f_n color_g shadow-sm bg-body",
        "style": "border-radius: 14px; border: 1px solid #D8E0F0 !important;",
    }))

    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={
        'name': "password",
        'placeholder': 'Password',
        "class": "form-control py-3 ps-4 pe-4 font_f_n color_g shadow-sm bg-body",
        "style": "border-radius: 14px; border: 1px solid #D8E0F0 !important;",
    }), required=False, )

    confirm_password = forms.CharField(label='Confirm Password', widget=forms.PasswordInput(attrs={
        'name': "confirm_password",
        'placeholder': 'Confirm Password',
        "class": "form-control py-3 ps-4 pe-4 font_f_n color_g shadow-sm bg-body",
        "style": "border-radius: 14px; border: 1px solid #D8E0F0 !important;",
    }), required=False, )

    role = forms.ChoiceField(
        choices=User.Role.choices,
        widget=forms.Select(attrs={
            'name': "role",
            "class": "form-control py-3 ps-4 pe-4 font_f_n color_g shadow-sm bg-body",
            "style": "border-radius: 14px; border: 1px solid #D8E0F0 !important;",
        }),
        required=True,
    )

    location = forms.ModelChoiceField(
        queryset=Location.objects.all(),
        widget=forms.Select(attrs={
            'name': "role",
            "class": "form-control py-3 ps-4 pe-4 font_f_n color_g shadow-sm bg-body",
            "style": "border-radius: 14px; border: 1px solid #D8E0F0 !important;",
        }),
        required=True
    )

    class Meta:
        model = User
        fields = ['full_name', 'email', 'birthdate', 'position', 'p_number', 'password', 'confirm_password', 'role',
                  'location']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password or confirm_password:
            if password != confirm_password:
                self.add_error('confirm_password', _('Parollar mos emas.'))
        return cleaned_data

    def save(self, commit=True):
        user = super().save(commit=False)
        password = self.cleaned_data.get('password')
        if password:
            user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user


class LoginForm(forms.Form):
    username = forms.CharField(required=True, widget=forms.TextInput(attrs={
        'id': 'input_username',
        'name': "username",
        'placeholder': 'youremail@gmail.com',
        "class": "form-control py-3 ps-4 font_f_n color_g z"
    }))

    password = forms.CharField(required=True, widget=forms.PasswordInput(attrs={
        'id': "password",
        'name': "password",
        'placeholder': 'Password',
        "class": "form-control py-3 ps-4 pe-5 font_f_n color_g",
    }))

    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        self.fields['password'].label = ""
