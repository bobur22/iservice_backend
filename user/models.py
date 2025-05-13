from django.db import models
from django.utils import timezone
from iservice.validators import validate_f_name, PhoneValidator
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from iservice.models import Location


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('You have not provided an email address.')

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('role', User.Role.DIRECTOR)

        return self.create_user(email, password, **extra_fields)

class User(AbstractBaseUser, PermissionsMixin):
    class Role(models.TextChoices):
        DIRECTOR = 'director', 'Director'
        EMPLOYEE = 'employee', 'Employee'

    email = models.EmailField(unique=True)

    full_name = models.CharField(max_length=255, verbose_name=_('toliq_ism'),
                                 help_text=_("Iltimos to'liq isimni yozing."),
                                 validators=[validate_f_name], blank=True, default='')
    p_number = models.CharField(max_length=13,
                                validators=[PhoneValidator()],
                                verbose_name=_('telefon_raqam'),
                                help_text=_('Iltimos, raqamni to\'g\'ri kiriting. Masalan: +998123456789'),
                                error_messages={'invalid': _('Iltimos, to‘g‘ri telefon raqamini kiriting!')},
                                blank=True, default='')
    birthdate = models.DateField(blank=True, null=True, verbose_name=_('birthdate'),)
    position = models.CharField(max_length=255, verbose_name=_('ish joyi'),
                                 help_text=_("Iltimos ish joyini kiriting."), blank=True, default='')

    role = models.CharField(
        max_length=20,
        choices=Role.choices,
        default=Role.EMPLOYEE
    )

    location = models.ForeignKey(
        Location,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name=_("location"),
        related_name="users"
    )

    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    date_joined = models.DateTimeField(default=timezone.now)
    last_login = models.DateTimeField(blank=True, null=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = []  # Email and password are prompted by default

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def get_full_name(self):
        return self.full_name

    def get_short_name(self):
        return self.full_name.split(' ')[0] or self.email.split('@')[0]

    # Role checking helpers
    def is_director(self):
        return self.role == self.Role.DIRECTOR

    def is_employee(self):
        return self.role == self.Role.EMPLOYEE
