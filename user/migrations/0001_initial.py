# Generated by Django 5.2 on 2025-05-11 15:26

import django.db.models.deletion
import django.utils.timezone
import iservice.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('iservice', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('full_name', models.CharField(blank=True, default='', help_text="Iltimos to'liq isimni yozing.", max_length=255, validators=[iservice.validators.validate_f_name], verbose_name='toliq_ism')),
                ('p_number', models.CharField(blank=True, default='', error_messages={'invalid': 'Iltimos, to‘g‘ri telefon raqamini kiriting!'}, help_text="Iltimos, raqamni to'g'ri kiriting. Masalan: +998123456789", max_length=13, validators=[iservice.validators.PhoneValidator()], verbose_name='telefon_raqam')),
                ('birthdate', models.DateField(blank=True, null=True, verbose_name='birthdate')),
                ('position', models.CharField(blank=True, default='', help_text='Iltimos ish joyini kiriting.', max_length=255, verbose_name='ish joyi')),
                ('role', models.CharField(choices=[('director', 'Director'), ('employee', 'Employee')], default='employee', max_length=20)),
                ('is_active', models.BooleanField(default=True)),
                ('is_superuser', models.BooleanField(default=False)),
                ('is_staff', models.BooleanField(default=False)),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now)),
                ('last_login', models.DateTimeField(blank=True, null=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('location', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='users', to='iservice.location', verbose_name='location')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'User',
                'verbose_name_plural': 'Users',
            },
        ),
    ]
