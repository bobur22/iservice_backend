from django.db import models
from django.utils.translation import gettext_lazy as _
from .validators import validate_email, PhoneValidator, validate_f_name
from django.conf import settings
from datetime import datetime
from django.core.exceptions import ValidationError
from decimal import Decimal


def validate_cost(value):
    value_str = str(value)
    if '.' in value_str and len(value_str.split('.')[-1]) > 1:
        raise ValidationError("Invalid cost format: don't use '.' as thousand separator.")

    return value



class Location(models.Model):
    location_name = models.CharField(max_length=50, verbose_name=_('location_name'), )
    location_description = models.TextField(verbose_name=_('location_description'), blank=True, null=True, )

    created_at = models.DateField(auto_now_add=True, verbose_name=_("yaratilgan vaqti"), null=True, blank=True)
    updated_at = models.DateField(auto_now=True, verbose_name=_("o'zgartirilgan vaqti"), null=True, blank=True)

    def __str__(self):
        return self.location_name

    class Meta:
        verbose_name = "Joylashuv"
        verbose_name_plural = "Joylashuvlar"


# Customer model.
class Customer(models.Model):
    full_name = models.CharField(max_length=50, verbose_name=_('toliq_ism'),
                                 help_text=_("Iltimos mijozning to'liq ismini kiriting."),
                                 validators=[validate_f_name])
    p_number = models.CharField(max_length=13,
                                validators=[PhoneValidator()],
                                verbose_name=_('telefon_raqam'),
                                help_text=_("Iltimos, telefon raqamni to'ri kiriting. Masalan: +998123456789"),
                                error_messages={'invalid': _('Iltimos, to‘g‘ri telefon raqamini kiriting!')}, )
    email = models.EmailField(verbose_name=_('pochta'), blank=True, null=True,
                              help_text=_("Iltimos, Email manzilingizni kiriting."), )
    description = models.TextField(verbose_name=_('tavsifi'), blank=True, null=True, )
    location = models.ForeignKey('Location', on_delete=models.SET_NULL, null=True, blank=True,
                                 verbose_name=_('joylashuv'))

    created_at = models.DateField(auto_now_add=True, verbose_name=_("yaratilgan vaqti"))
    updated_at = models.DateField(auto_now=True, verbose_name=_("o'zgartirilgan vaqti"))

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = "Mijoz"
        verbose_name_plural = "Mijozlar"


class Task(models.Model):
    class Status(models.TextChoices):
        ToDo = 'To Do', 'todo'
        Progress = 'In Progress', 'progress'
        Review = 'In Review', 'review'
        Done = 'Done', 'done'

    class Payment_type(models.TextChoices):
        Cash = 'Cash', 'cash'
        Card = 'Card', 'card'
        Process = 'Process', 'process'

    task_title = models.CharField(max_length=200, verbose_name=_('task title'), )

    role = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.ToDo
    )
    deadline = models.DateField(verbose_name=_('deadline'))
    price = models.DecimalField(max_digits=12, decimal_places=1, verbose_name=_('price'), validators=[validate_cost])

    payment_t = models.CharField(
        max_length=20,
        choices=Payment_type.choices,
        default=Payment_type.Process
    )
    cost = models.DecimalField(max_digits=12, decimal_places=1, verbose_name=_('cost'), default=0, validators=[validate_cost], null=True, blank=True)
    program = models.CharField(max_length=200, verbose_name=_('program'), default=".", null=True, blank=True)
    program_sum = models.DecimalField(max_digits=12, decimal_places=1, verbose_name=_('program_summ'), default=0, validators=[validate_cost], null=True, blank=True)

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name=_('user'), default=1)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, verbose_name=_('customer'), )

    location = models.ForeignKey('Location', on_delete=models.SET_NULL, null=True, blank=True,
                                 verbose_name=_('joylashuv'))

    created_at = models.DateField(auto_now_add=True, verbose_name=_("yaratilgan vaqti"))
    updated_at = models.DateField(auto_now=True, verbose_name=_("o'zgartirilgan vaqti"))

    def __str__(self):
        return self.task_title

    class Meta:
        verbose_name = "Vazifa"
        verbose_name_plural = "Vazifalar"
