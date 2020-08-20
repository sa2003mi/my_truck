from django.urls import path
from django.conf.urls import url
from . import views


app_name = 'contact'
urlpatterns = [
    path('', views.Contact, name='contact_us'),
    


]
