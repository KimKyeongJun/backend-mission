from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
from market.models import Market


class User(AbstractUser):
    first_name = None
    last_name = None
    name = models.CharField(max_length=10, default='')
    market_yn = models.BooleanField(default=False)
    market_id = models.OneToOneField(Market, on_delete=models.CASCADE, null=True, blank=True)
    pass





class RefreshStorage(models.Model):
    hash_value = models.CharField(max_length=255)
    refresh_token = models.CharField(max_length=500)
    user_fk = models.ForeignKey(User, on_delete=models.CASCADE, db_column='user_fk', default=1)
