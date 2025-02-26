from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager, Group, Permission

# Create your models here.

class UserManager(BaseUserManager):
    def create_user(self, email, password, username = None):
        if not email:
            raise ValueError("Email is Required")
        user = self.model(username = username, email = self.normalize_email(email))
        user.set_password(password)
        user.save(using = self._db)
        return user
    
    def create_superuser( self, email, password, username = None): # for admin creation to accesee the admin panel
        user = self.create_user(email = email, password = password, username = username)
        user.is_staff = True
        user.is_superuser = True
        user.save(using = self._db)
        return user

class User(AbstractUser):
    username = models.CharField(max_length=255, blank = True, null = True)
    email = models.EmailField(unique = True, max_length = 255)
    objects = UserManager()
    USERNAME_FIELD = 'email' # the field required for authentication
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.username


