from django.urls import path
from django.conf.urls import url
from . import views, api


app_name = 'driver'
urlpatterns = [
    path('', views.DriverList.as_view(), name='driver_list'),
    path('add/', views.DriverCreate.as_view(), name='driver_create'),
    path('<int:pk>/', views.DriverDetail.as_view(), name='driver_detail'),
    path('<int:pk>/update/', views.DriverUpdate.as_view(), name='driver_update'),
    path('<int:pk>/delete/', views.DriverDelete.as_view(), name='driver_delete'),

    ## api
    path('api/driver/', api.driver_list_api, name='driver_list_api'),
    path('api/driver/<int:id>/', api.driver_detail_api,
         name='driver_detail_api'),

    ## class based view
    path('api/Driver/', api.Driver_list_Api.as_view(),
         name='Driver_list_Api'),
    path('api/Driver/<int:pk>/', api.Driver_detail_Api.as_view(),
         name='Driver_detail_Api'),



]



