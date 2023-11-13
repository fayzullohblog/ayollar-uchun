from django.db import models
from django.contrib.auth.models import AbstractUser, AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.core.validators import RegexValidator

from .manager import UserManager
# Create your models here.


class Job(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class GenderChoise(models.Choices):
    MALE = 'Erkak'
    FEMALE = 'Ayol'


class User(AbstractBaseUser, PermissionsMixin):

    _validate_phone = RegexValidator(
        regex=r'^998[0-9]{9}$',
        message="Telefon raqamingiz 9 bilan boshlanishi va 12 ta belgidan iborat bo'lishi kerak. Masalan: 998901235476"
    )
    gender = models.CharField(
        max_length=255, choices=GenderChoise.choices, default=GenderChoise.FEMALE)

    first_name = models.CharField(max_length=50, null=True, blank=True)
    last_name = models.CharField(max_length=50, null=True, blank=True)

    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)

    birth_day = models.DateField(blank=True, null=True)
    phone_number = models.CharField(
        max_length=15, unique=True, validators=[_validate_phone])
    email = models.EmailField(null=True, blank=True)

    country = models.CharField(max_length=255, blank=True, null=True)
    region = models.CharField(max_length=255, blank=True, null=True)
    postcode = models.CharField(max_length=10, blank=True, null=True)

    address = models.CharField(max_length=255, blank=True, null=True)

    instagram = models.CharField(max_length=255, blank=True, null=True)
    imkon_uz = models.CharField(max_length=255, blank=True, null=True)
    linkedin = models.CharField(max_length=255, blank=True, null=True)

    workplace = models.CharField(max_length=255, blank=True, null=True)
    job = models.ForeignKey(
        Job, on_delete=models.CASCADE, blank=True, null=True)
    about = models.TextField(blank=True, null=True)

    USERNAME_FIELD = 'phone_number'

    objects = UserManager()

    def get_full_name(self):
        return self.first_name + ' ' + self.last_name

    def __str__(self) -> str:
        return self.get_full_name()

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    def __str__(self) -> str:
        return self.phone_number

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_superuser
