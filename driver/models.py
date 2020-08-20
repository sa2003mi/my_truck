from django.db import models
from django.urls import reverse
from django.core.validators import RegexValidator
from location_field.models.plain import PlainLocationField
from django.contrib.auth.models import User
from sorl.thumbnail import ImageField
from django.utils.translation import ugettext_lazy, activate, get_language




# Create your models here.

class Driver(models.Model):
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    image = ImageField(upload_to="driver_img")
    phone_regex = RegexValidator(
        regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(
        validators=[phone_regex], max_length=17, blank=True)  # validators should be a list
    city = models.CharField(max_length=255)
    location = PlainLocationField(based_fields=['city'], zoom=7)
    created_by = models.ForeignKey(User , related_name = 'driver' , on_delete = models.CASCADE )


    

    class Meta:
        verbose_name = ("Driver")
        verbose_name_plural = ("Drivers")

    def __str__(self):
        return self.first_name

    def get_absolute_url(self):
        return reverse("driver:driver_detail", kwargs={"pk": self.pk})

