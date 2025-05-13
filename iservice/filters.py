import django_filters
from django import forms
from .models import Customer, Task, Location
from user.models import User

"""
    Custom Widgets start.
"""


class CustomRangeWidget(forms.MultiWidget):
    def __init__(self, attrs=None):
        widgets = [
            forms.NumberInput(attrs={
                'placeholder': 'Min price',
                'class': 'col-6 py-3 ps-4 pe-4 font_f_n color_g shadow-sm bg-body',
                'style': 'border-radius: 14px; border: 1px solid #D8E0F0 !important;',
            }),
            forms.NumberInput(attrs={
                'placeholder': 'Max price',
                'class': 'col-6 py-3 ps-4 pe-4 font_f_n color_g shadow-sm bg-body',
                'style': 'border-radius: 14px; border: 1px solid #D8E0F0 !important;',
            }),
        ]
        super().__init__(widgets, attrs)

    def decompress(self, value):
        if value:
            return [value.start, value.stop]
        return [None, None]


class CustomDateRangeWidget(forms.MultiWidget):
    def __init__(self, attrs=None):
        widgets = [
            forms.DateInput(attrs={
                'type': 'date',
                'placeholder': 'Start date',
                'class': 'col-6 py-3 ps-4 pe-4 font_f_n color_g shadow-sm bg-body',
                'style': 'border-radius: 14px; border: 1px solid #D8E0F0 !important;',
            }),
            forms.DateInput(attrs={
                'type': 'date',
                'placeholder': 'End date',
                'class': 'col-6 py-3 ps-4 pe-4 font_f_n color_g shadow-sm bg-body',
                'style': 'border-radius: 14px; border: 1px solid #D8E0F0 !important;',
            }),
        ]
        super().__init__(widgets, attrs)

    def decompress(self, value):
        if value:
            return [value.start, value.stop]
        return [None, None]


"""
    Custom Widgets end.
"""


class CustomerFilter(django_filters.FilterSet):
    full_name = django_filters.CharFilter(
        lookup_expr='icontains',
        widget=forms.TextInput(attrs={
            'placeholder': 'Full Name',
            'class': 'form-control py-3 ps-4 pe-4 font_f_n color_g shadow-sm bg-body',
            'style': 'border-radius: 14px; border: 1px solid #D8E0F0 !important;',
        })
    )

    p_number = django_filters.CharFilter(
        lookup_expr='icontains',
        widget=forms.TextInput(attrs={
            'placeholder': 'Phone Number',
            'class': 'form-control py-3 ps-4 pe-4 font_f_n color_g shadow-sm bg-body',
            'style': 'border-radius: 14px; border: 1px solid #D8E0F0 !important;',
        })
    )

    location = django_filters.ModelChoiceFilter(
        queryset=Location.objects.all(),
        widget=forms.Select(attrs={
            "class": "form-control py-3 ps-4 pe-4 font_f_n color_g shadow-sm bg-body",
            "style": "border-radius: 14px; border: 1px solid #D8E0F0 !important;",
        }),
        empty_label="All",
        required=False,
    )

    email = django_filters.CharFilter(
        lookup_expr='icontains',
        widget=forms.TextInput(attrs={
            'placeholder': 'Email',
            'class': 'form-control py-3 ps-4 pe-4 font_f_n color_g shadow-sm bg-body',
            'style': 'border-radius: 14px; border: 1px solid #D8E0F0 !important;',
        })
    )

    class Meta:
        model = Customer
        fields = ['full_name', 'p_number', 'email']


class UserFilter(django_filters.FilterSet):
    full_name = django_filters.CharFilter(
        lookup_expr='icontains',
        widget=forms.TextInput(attrs={
            'placeholder': 'Full Name',
            'class': 'form-control py-3 ps-4 pe-4 font_f_n color_g shadow-sm bg-body',
            'style': 'border-radius: 14px; border: 1px solid #D8E0F0 !important;',
        })
    )

    email = django_filters.CharFilter(
        lookup_expr='icontains',
        widget=forms.TextInput(attrs={
            'placeholder': 'Email',
            'class': 'form-control py-3 ps-4 pe-4 font_f_n color_g shadow-sm bg-body',
            'style': 'border-radius: 14px; border: 1px solid #D8E0F0 !important;',
        })
    )

    p_number = django_filters.CharFilter(
        lookup_expr='icontains',
        widget=forms.TextInput(attrs={
            'placeholder': 'Phone Number',
            'class': 'form-control py-3 ps-4 pe-4 font_f_n color_g shadow-sm bg-body',
            'style': 'border-radius: 14px; border: 1px solid #D8E0F0 !important;',
        })
    )

    position = django_filters.CharFilter(
        lookup_expr='icontains',
        widget=forms.TextInput(attrs={
            'placeholder': 'Position',
            'class': 'form-control py-3 ps-4 pe-4 font_f_n color_g shadow-sm bg-body',
            'style': 'border-radius: 14px; border: 1px solid #D8E0F0 !important;',
        })
    )

    location = django_filters.ModelChoiceFilter(
        queryset=Location.objects.all(),
        widget=forms.Select(attrs={
            "class": "form-control py-3 ps-4 pe-4 font_f_n color_g shadow-sm bg-body",
            "style": "border-radius: 14px; border: 1px solid #D8E0F0 !important;",
        }),
        empty_label="All",
        required=False,
    )

    class Meta:
        model = User
        fields = ['full_name', 'email', 'p_number', 'position', 'location']


class TasksFilter(django_filters.FilterSet):
    task_title = django_filters.CharFilter(
        lookup_expr='icontains',
        widget=forms.TextInput(attrs={
            'placeholder': 'Task Name',
            'class': 'form-control py-3 ps-4 pe-4 font_f_n color_g shadow-sm bg-body',
            'style': 'border-radius: 14px; border: 1px solid #D8E0F0 !important;'
        }),
        required=False,
    )

    role = django_filters.ChoiceFilter(
        choices=Task.Status.choices,
        widget=forms.Select(attrs={
            'class': 'form-control py-3 ps-4 pe-4 font_f_n color_g shadow-sm bg-body',
            'style': 'border-radius: 14px; border: 1px solid #D8E0F0 !important;'
        }),
        empty_label='All',
        required=False,
    )

    deadline = django_filters.DateFromToRangeFilter(
        label='Deadline Range',
        widget=CustomDateRangeWidget(),
        required=False
    )

    price = django_filters.RangeFilter(
        label='Price Range',
        widget=CustomRangeWidget(),
        required=False
    )

    payment_t = django_filters.ChoiceFilter(
        choices=Task.Payment_type.choices,
        widget=forms.Select(attrs={
            'class': 'form-control py-3 ps-4 pe-4 font_f_n color_g shadow-sm bg-body',
            'style': 'border-radius: 14px; border: 1px solid #D8E0F0 !important;'
        }),
        empty_label='All',
        required=False,
    )

    cost = django_filters.RangeFilter(
        label='Cost Range',
        widget=CustomRangeWidget(),
        required=False
    )

    program = django_filters.CharFilter(
        lookup_expr='icontains',
        widget=forms.TextInput(attrs={
            'placeholder': 'Program Name',
            'class': 'form-control py-3 ps-4 pe-4 font_f_n color_g shadow-sm bg-body',
            'style': 'border-radius: 14px; border: 1px solid #D8E0F0 !important;'
        }),
        required=False,
    )

    program_sum = django_filters.RangeFilter(
        label='Program Sum Range',
        widget=CustomRangeWidget(),
        required=False
    )

    customer = django_filters.ModelChoiceFilter(
        queryset=Customer.objects.none(),  # Empty by default
        widget=forms.Select(attrs={
            'class': 'form-control py-3 ps-4 pe-4 font_f_n color_g shadow-sm bg-body',
            'style': 'border-radius: 14px; border: 1px solid #D8E0F0 !important;'
        }),
        required=False
    )

    location = django_filters.ModelChoiceFilter(
        queryset=Location.objects.all(),
        widget=forms.Select(attrs={
            'class': 'form-control py-3 ps-4 pe-4 font_f_n color_g shadow-sm bg-body',
            'style': 'border-radius: 14px; border: 1px solid #D8E0F0 !important;'
        }),
        empty_label='All Locations',
        required=False
    )

    class Meta:
        model = Task
        # fields = ['task_title', 'role', 'customer', 'deadline', 'price', 'location']
        fields = ['task_title', 'role', 'deadline', 'price', 'payment_t', 'cost', 'program',
                  'program_sum', 'customer']

    def __init__(self, *args, **kwargs):
        request = kwargs.pop('request', None)
        super().__init__(*args, **kwargs)

        if request and request.user and not request.user.is_superuser:
            self.filters['customer'].queryset = Customer.objects.filter(location=request.user.location)
        else:
            self.filters['customer'].queryset = Customer.objects.all()
