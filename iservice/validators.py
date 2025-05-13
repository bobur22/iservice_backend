from django.core.exceptions import ValidationError
import re
import phonenumbers
from django.utils.deconstruct import deconstructible
from django.utils.translation import gettext_lazy as _
from datetime import datetime, date


def validate_email(value):
    """Validate email"""

    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if not re.match(pattern, value):
        raise ValidationError(_("Enter a valid email address."), params={"value": value})


def validate_f_name(value):
    """Validate Full Name"""
    num = 0
    for char in value.split(' '):
        num+=1

    if num >= 2:
        for i in value.split(' '):
            if i.isdigit():
                raise ValidationError(_("Toʻliq ism kiriting.(raqamlarsiz)"))
    else:
        raise ValidationError(_("Ism va familiyani o'z ichiga olgan to'liq ismni kiriting"))


@deconstructible
class PhoneValidator:
    requires_context = False

    @staticmethod
    def clean(value):
        return re.sub('[^0-9+]+', '', value)

    @staticmethod
    def validate(value):
        try:
            z = phonenumbers.parse(value)  # 998944009080
            if not phonenumbers.is_valid_number(z):
                return False
        except:
            return False

        if len(value) != 13 or not value.startswith("+998"):
            return False

        return True

    def __call__(self, value):
        if not PhoneValidator.validate(value):
            raise ValidationError(_("Kiritilgan qiymat telefon raqami emas."))


def validate_date(value):
    """Validate date"""
    x = str(value)
    try:
        if x != datetime.strptime(x, "%Y-%m-%d"):
            x = x.split("-")
    except ValueError:
        raise ValueError("Incorrect data format, should be YYYY-MM-DD")


VALID_IMAGE_EXTENSIONS = [
    ".jpg",
    ".jpeg",
    ".png",
]


def valid_url_extension(value, extension_list=VALID_IMAGE_EXTENSIONS):
    value = str(value)
    print(value)
    # http://stackoverflow.com/a/10543969/396300
    if not (any([value.endswith(e) for e in extension_list])):
        raise ValidationError("Please upload a valid image extension")