from django.db import models
from gyms.models import Membership
from accounts.models import User

# Create your models here.


class Payment(models.Model):
    STATUS_CHOICES = [
        ("pending", "Pending"),
        ("completed", "Completed"),
        ("failed", "Failed"),
    ]
    PAYMENT_METHOD_CHOICES = [
        ("card", "Card"),
        ("upi", "UPI"),
        ("cash", "Cash"),
        ("net_banking", "Net Banking"),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user")
    membership = models.ForeignKey(
        Membership, on_delete=models.CASCADE, related_name="membership"
    )
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="pending")
    method = models.CharField(
        max_length=20, choices=PAYMENT_METHOD_CHOICES, default="cash"
    )
    payment_date = models.DateTimeField(auto_now_add=True)
