from django.urls import path
from django.conf.urls import url
from . import views , api



app_name='service'
urlpatterns = [
    path('service/', views.ServiceList.as_view(), name='index'),
    path('../ar/service/', views.ServiceList.as_view(), name='service_list'),
    path('../en/service/', views.ServiceList.as_view(), name='index'),
    path('service/<int:pk>/', views.ServiceDetail.as_view(), name='service_detail'),
    
    ## api
    path('api/service/', api.service_list_api, name='service_list_api'),
    path('api/service/<int:id>/', api.service_detail_api,
         name='service_detail_api'),

    ## class based view
    path('api/Service/', api.Service_list_Api.as_view(),
         name='Service_list_Api'),
    path('api/Service/<int:pk>/', api.Service_detail_Api.as_view(),
         name='Service_detail_Api'),
    
    
]
