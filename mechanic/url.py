from django.urls import path
from django.conf.urls import url
from . import views, api



app_name = 'mechanic'
urlpatterns = [
    path('', views.MechanicList.as_view(), name='mechanic_list'),
    path('add/', views.MechanicCreate.as_view(), name='mechanic_create'),
    path('<int:pk>/', views.MechanicDetail.as_view(), name='mechanic_detail'),
    path('<int:pk>/update/', views.MechanicUpdate.as_view(), name='mechanic_update'),
    path('<int:pk>/delete/', views.MechanicDelete.as_view(), name='mechanic_delete'),

    ## api
    path('api/mechanic/', api.mechanic_list_api, name='mechanic_list_api'),
    path('api/mechanic/<int:id>/', api.mechanic_detail_api,
         name='mechanic_detail_api'),

    ## class based view
    path('api/Mechanic/', api.Mechanic_list_Api.as_view(),
         name='Mechanic_list_Api'),
    path('api/Mechanic/<int:pk>/', api.Mechanic_detail_Api.as_view(),
         name='Mechanic_detail_Api'),


]
