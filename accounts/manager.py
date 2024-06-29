from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, phone_number, email, password, f_name=None, l_name=None, address=None):
        if not phone_number:
            raise ValueError('phone number must be set')

        if not email:
            raise ValueError('email must be set')

        user = self.model(phone_number=phone_number, email=email, f_name=f_name, l_name=l_name, address=address)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, phone_number, email, password, f_name=None, l_name=None, address=None):
        user = self.create_user(phone_number, email, password, f_name, l_name, address)
        user.is_admin = True
        user.save(using=self._db)
        return user
