from django.contrib.auth.models import AbstractUser
from django.db import models

class Account(AbstractUser):
    ACCOUNT_TYPE_CHOICES = [
        ('seller', 'Seller'),
        ('buyer', 'Buyer'),
        ('admin', 'Admin'),
        ('staff', 'Staff'),
        ('basic', 'Basic'),
    ]

    account_type = models.CharField(
        max_length=10,
        choices=ACCOUNT_TYPE_CHOICES,
        default='basic',
    )

    def __str__(self):
        return self.username
