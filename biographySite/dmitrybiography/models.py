from django.db import models

# Create your models here.


class UserEmails(models.Model):
    email = models.CharField(max_length=100, verbose_name='Email')