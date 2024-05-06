from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

class CustomUser(AbstractUser):
    profile_picture = models.ImageField(upload_to='profile_pictures/', null=True, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    
    # Definindo related_name para evitar conflitos com auth.User
    groups = models.ManyToManyField(
        Group,
        related_name='customuser_set',
        blank=True
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='customuser_set',
        blank=True
    )
    

    def __str__(self):
        return self.username
