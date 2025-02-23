from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager, Group, Permission
# Create your models here.
class UserManager(BaseUserManager):
    def create_user(self, email, password):
        if not email:
            raise ValueError("Email is Required")
        user = self.model(email = self.normalize_email(email))
        user.set_password(password)
        user.save(using = self._db)
        return user
    
    def create_superuser(self, email, password):
        user = self.create_user(email = email, password = password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using = self._db)
        return user

class User(AbstractUser):
    email = models.EmailField(unique = True, max_length = 255)
    username = models.CharField(max_length=255, blank=True, null=True)
    objects = UserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    groups = models.ManyToManyField(
        Group,
        related_name='custom_user_groups',  # Unique related_name
        blank=True
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='custom_user_permissions',  # Unique related_name
        blank=True
    )

    def __str__(self):
        return self.username
