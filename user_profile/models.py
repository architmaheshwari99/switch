from django.db import models

from account.models import Account

# Create your models here.
class Profile(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    user = models.OneToOneField(Account, on_delete=models.CASCADE)
    bio = models.CharField(max_length=255, blank=True, null=True)
    is_verified = models.BooleanField(default=False)
    phone_no = models.CharField(max_length=10, blank=True, null=True)
    achievements = models.CharField(max_length=256, blank=True, null=True)
    profile_photo = models.ImageField(upload_to='profile/', blank=True)
    daily_credit = models.IntegerField(default=10)
    company_email_address = models.EmailField(max_length=255, blank=True, null=True)
    resume = models.FileField(upload_to='profile/')

    def __str__(self):
        return self.user.email 

    
