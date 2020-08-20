from django.db import models
from django.utils.translation import gettext_lazy, activate, get_language

# Create your models here.


class Info(models.Model):
    place = models.CharField(max_length=150)
    phone_number = models.CharField(max_length=150)
    email = models.EmailField(max_length=250)

    class Meta:
        verbose_name = ("Info")
        verbose_name_plural = ("Infos")

    def __str__(self):
        return self.email
