from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext_lazy, activate, get_language




# Create your models here.

class Service(models.Model):
    
    MECHANIC = 'MIC'
    DRIVER = 'DRI'
    AUTO_ROOF ='AUR'
    SPARE_PARTS ='SPR'
    OLD_PARTS = 'OLD'
    SERVICE_CHOICES =[
       ( MECHANIC,'mechanic'),
       (AUTO_ROOF,'auto_roof'),
       (SPARE_PARTS,'spare_parts'),
       (OLD_PARTS, 'old_parts'),
       (DRIVER ,'driver')
    ] 
    service = models.CharField(max_length = 10 ,choices=SERVICE_CHOICES,default=MECHANIC)
    

    class Meta:
        verbose_name = ("Service")
        verbose_name_plural = ("Services")

    def __str__(self):
        return self.service

    def get_absolute_url(self):
        return reverse("Service_detail", kwargs={"pk": self.pk})





    
