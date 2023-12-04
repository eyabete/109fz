# Create your models here.
# models.py

from django.db import models
from django.contrib.auth.models import User
from item.models import Item

class Purchase(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)  # Adjust this based on your item model
    quantity = models.PositiveIntegerField()
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    # Add other fields as needed (e.g., purchase date)
