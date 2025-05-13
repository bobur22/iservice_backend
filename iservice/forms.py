from django import forms
from .models import Customer, Task, Location

class CustomerForm(forms.ModelForm):

    full_name = forms.CharField(required=True, widget=forms.TextInput(attrs={
        'name': "full_name",
        'placeholder': 'Full Name',
        "class": "form-control py-3 ps-4 pe-4 font_f_n color_g shadow-sm bg-body",
        "style": "border-radius: 14px; border: 1px solid #D8E0F0 !important;",
    }))

    p_number = forms.CharField(required=True, widget=forms.TextInput(attrs={
        'name': "emp_number",
        'placeholder': 'Phone Number',
        "class": "form-control py-3 ps-4 pe-4 font_f_n color_g shadow-sm bg-body",
        "style": "border-radius: 14px; border: 1px solid #D8E0F0 !important;",
    }))

    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={
        'name': "emp_email",
        'placeholder': 'Email',
        "class": "form-control py-3 ps-4 pe-4 font_f_n color_g shadow-sm bg-body",
        "style": "border-radius: 14px; border: 1px solid #D8E0F0 !important;",
    }))

    description = forms.CharField(required=True, widget=forms.Textarea(attrs={
        'name': "description",
        'placeholder': 'Description',
        "class": "form-control py-3 ps-4 pe-4 font_f_n color_g shadow-sm bg-body",
        "style": "border-radius: 14px; border: 1px solid #D8E0F0 !important;",
    }))

    location = forms.ModelChoiceField(
        queryset=Location.objects.all(),
        widget=forms.Select(attrs={
            'name': 'location',
            "class": "form-control py-3 ps-4 pe-4 font_f_n color_g shadow-sm bg-body",
            "style": "border-radius: 14px; border: 1px solid #D8E0F0 !important;",
        }),
        required=False,
    )

    class Meta:
        model = Customer
        fields = ['full_name', 'p_number', 'email', 'description']


class TasksForm(forms.ModelForm):
    task_title = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={
            'placeholder': 'Task Name',
            'class': 'form-control py-3 ps-4 pe-4 font_f_n color_g shadow-sm bg-body',
            'style': 'border-radius: 14px; border: 1px solid #D8E0F0 !important;'
        })
    )

    role = forms.ChoiceField(
        choices=Task.Status.choices,
        widget=forms.Select(attrs={
            'class': 'form-control py-3 ps-4 pe-4 font_f_n color_g shadow-sm bg-body',
            'style': 'border-radius: 14px; border: 1px solid #D8E0F0 !important;'
        }),
        required=True
    )

    deadline = forms.DateField(
        widget=forms.DateInput(attrs={
            'type': 'date',
            'placeholder': 'Deadline',
            'class': 'form-control py-3 ps-4 pe-4 font_f_n color_g shadow-sm bg-body',
            'style': 'border-radius: 14px; border: 1px solid #D8E0F0 !important;'
        }, format='%Y-%m-%d'),
        input_formats=['%Y-%m-%d'],
        required=True,
    )

    price = forms.DecimalField(
        max_digits=11,
        decimal_places=1,
        required=True,
        widget=forms.NumberInput(attrs={
            'placeholder': 'Price',
            'class': 'form-control py-3 ps-4 pe-4 font_f_n color_g shadow-sm bg-body',
            'style': 'border-radius: 14px; border: 1px solid #D8E0F0 !important;'
        })
    )

    payment_t = forms.ChoiceField(
        choices=Task.Payment_type.choices,
        widget=forms.Select(attrs={
            'class': 'form-control py-3 ps-4 pe-4 font_f_n color_g shadow-sm bg-body',
            'style': 'border-radius: 14px; border: 1px solid #D8E0F0 !important;'
        }),
        required=True
    )

    cost = forms.DecimalField(
        max_digits=11,
        decimal_places=1,
        required=False,
        widget=forms.NumberInput(attrs={
            'placeholder': 'Price',
            'class': 'form-control py-3 ps-4 pe-4 font_f_n color_g shadow-sm bg-body',
            'style': 'border-radius: 14px; border: 1px solid #D8E0F0 !important;'
        })
    )

    program = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={
            'placeholder': 'Task Name',
            'class': 'form-control py-3 ps-4 pe-4 font_f_n color_g shadow-sm bg-body',
            'style': 'border-radius: 14px; border: 1px solid #D8E0F0 !important;'
        })
    )
    program_sum = forms.DecimalField(
        max_digits=11,
        decimal_places=1,
        required=False,
        widget=forms.NumberInput(attrs={
            'placeholder': 'Price',
            'class': 'form-control py-3 ps-4 pe-4 font_f_n color_g shadow-sm bg-body',
            'style': 'border-radius: 14px; border: 1px solid #D8E0F0 !important;'
        })
    )

    customer = forms.ModelChoiceField(
        queryset=Customer.objects.none(),  # Empty initially
        widget=forms.Select(attrs={
            'class': 'form-control py-3 ps-4 pe-4 font_f_n color_g shadow-sm bg-body',
            'style': 'border-radius: 14px; border: 1px solid #D8E0F0 !important;'
        }),
        required=True
    )

    location = forms.ModelChoiceField(
        queryset=Location.objects.all(),
        widget=forms.Select(attrs={
            'name': 'location',
            "class": "form-control py-3 ps-4 pe-4 font_f_n color_g shadow-sm bg-body",
            "style": "border-radius: 14px; border: 1px solid #D8E0F0 !important;",
        }),
        required=False,
    )

    class Meta:
        model = Task
        fields = ['task_title', 'role', 'deadline', 'price', 'payment_t', 'cost', 'program', 'program_sum', 'customer']

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)

        if user and not user.is_superuser:
            self.fields['customer'].queryset = Customer.objects.filter(location=user.location)
        else:
            self.fields['customer'].queryset = Customer.objects.all()


class LocationForm(forms.ModelForm):
    class Meta:
        model = Location
        fields = ['location_name']