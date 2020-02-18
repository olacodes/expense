from django.db import models

from .user import User

class Expense(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)
    value = models.DecimalField(max_digits=10, decimal_places=2)
    reason = models.TextField()
    last_modified = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-last_modified']
