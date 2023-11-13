from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, phone_number, first_name=None, last_name=None, password=None,):
        if not phone_number:
            raise ValueError("User must have a phone number")
        if not password:
            raise ValueError("User must have a Password")

        user = self.model(
            phone_number=phone_number,
            first_name=first_name,
            last_name=last_name,
        )

        user.set_password(password)  # change password to hash
        user.save(using=self._db)
        return user

    def create_superuser(self, phone_number, first_name=None, last_name=None, password=None):
        user = self.create_user(
            phone_number=phone_number,
            password=password,
            first_name=first_name,
            last_name=last_name,

        )
        user.is_superuser = True
        user.save(using=self._db)
        return user
