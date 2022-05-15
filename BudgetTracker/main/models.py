from tkinter import CASCADE
from typing import Optional
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class BudgetItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='budgetitem', null=True)
    date = models.DateField()
    name = models.CharField(max_length=200)
    amount = models.DecimalField(decimal_places=2, max_digits=99)
    iscost = models.BooleanField()


    def __str__(self):
        return self.name

