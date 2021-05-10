from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager
from django.utils.timezone import now


class UserProfileManage(BaseUserManager):
    """ Manage para perfiles de usuairo se crean las funciones para los usuairo"""

    def create_user(self, email, name, surname, password=None):
        """ Crear nuevo usuario """
        if not email:
            raise ValueError("Email is required")
        if not name:
            raise ValueError('Name is required')
        if not surname:
            raise ValueError('Surname is required')

        email = self.normalize_email(email)
        user = self.model(date=now(), email=email, name=name, surname=surname)

        user.set_password(password)
        user.save(using=self._db)

        return user

    """ Super uario """

    def create_superuser(self, email, name, surname, password):
        user = self.create_user(email, name, surname, password)

        user.is_superuser = True
        user.is_staff = True
        """Guadamos en bbdd"""
        user.save(using=self._db)

        return user


# Create your models here.
# No incluimos el campo is_superUser porque lo hacemos mediante el PermissionMixin
class UserProfile(AbstractBaseUser, PermissionsMixin):
    """ Modelo base de datos para usuarios en el sistema """
    #id = models.CharField(max_length=255, unique=True, primary_key=True, auto_created=True)
    date = models.DateTimeField()
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255, unique=True)
    surname = models.CharField(max_length=255, unique=True)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    object = UserProfileManage()

    # Los nombres tiene que ser así si no no funciona y no te pregunta los campos a la hora de crear el usuario
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'surname']

    def get_full_name(self):
        return self.name

    def get_short_name(self):
        return self.name

    def __str__(self):
        return self.email
