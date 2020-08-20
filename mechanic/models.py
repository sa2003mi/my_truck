from django.db import models
from django.urls import reverse
from django.core.validators import RegexValidator
from location_field.models.plain import PlainLocationField # when we use any kind of location field
from django.contrib.auth.models import User
from sorl.thumbnail import ImageField
from mapbox_location_field.models import LocationField # when we use a mapbox location only 
from django.utils.translation import ugettext_lazy, activate, get_language



# Create your models here.

class Mechanic(models.Model):
    first_name = models.CharField(max_length = 150)
    last_name = models.CharField(max_length = 150)
    image = ImageField(upload_to="mechanic_img")
    phone_regex = RegexValidator(
        regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(
        validators=[phone_regex], max_length=17, blank=True)  # validators should be a list
    city = models.CharField(max_length=255)
    location = LocationField(
        map_attrs={"center": [0, 0], "marker_color": "blue"})
    created_by = models.ForeignKey(User , related_name = 'mechanic' , on_delete = models.CASCADE )

    

    class Meta:
        verbose_name = ("Mechanic")
        verbose_name_plural = ("Mechanics")

    def __str__(self):
        return self.first_name

    def get_absolute_url(self):
        return reverse("mechanic:mechanic_detail", kwargs={"pk": self.pk})

    
