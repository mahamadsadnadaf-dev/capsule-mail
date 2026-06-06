from django.db import models
from django.contrib.auth.models import User

class Letter(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE )
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    delivery_date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.URLField(blank=True, null=True)
    delivered = models.BooleanField(default=False)

    def __str__(self):
        return self.subject