from datetime import timedelta
from django.utils import timezone
from django.db import models
from accounts.models import User
from django.conf import settings


# Create your models here.
class Gym(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    owner = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="gyms"
    )


class Plan(models.Model):
    # gym = models.ForeignKey(Gym, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    duration_days = models.IntegerField(default=30)


class Membership(models.Model):
    STATUS_CHOICES = [
        ("active", "Active"),
        ("expired", "Expired"),
        ("cancelled", "Cancelled"),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    plan = models.ForeignKey(Plan, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="active")
    start_date = models.DateField(default=timezone.localdate)
    end_date = models.DateField(null=True, blank=True)
    is_active = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        if not self.end_date:
            self.end_date = self.start_date + timedelta(days = self.plan.duration_days)
        super().save(*args, **kwargs)
