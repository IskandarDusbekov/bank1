"""
Bank app modeli
"""
from django.db import models

# Create your models here.
class Card(models.Model):
    """
    Card Model
    """
    S_Active="active"
    S_Inactive="inactive"
    S_Expired="expired"

    STATUS_CHOICES = [
        (S_Active, "Active"),
        (S_Inactive, "Inactive"),
        (S_Expired, "Expired"),
    ]

    card_number = models.CharField(max_length=16, unique=True)
    phone =models.CharField(max_length=16,null=True,blank=True)
    expire = models.DateField()
    status = models.CharField(choices=STATUS_CHOICES, max_length=10)
    balance = models.DecimalField(decimal_places=2, max_digits=20)

    def __str__(self):
        return self.card_number

