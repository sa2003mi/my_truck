from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save  
from django.dispatch import receiver
import datetime
from sorl.thumbnail import ImageField
from django.urls import  reverse
from django.utils.translation import ugettext_lazy, activate, get_language
# Create your models here.


class Profile(models.Model):
   user =  models.OneToOneField(User, on_delete=models.CASCADE)
   image = ImageField(upload_to="profile_img")
   city = models.CharField(max_length=255)
   join_date = models.DateTimeField( auto_now_add=True)
   bio = models.TextField(max_length=500, blank=True)

   def __str__(self):
       return str(self.user)
   

@receiver(post_save, sender=User)
def create_user_profile(sender,instance,created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    

   
   
    
