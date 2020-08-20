from django.urls import path
from django.conf.urls import url
from . import views , api


app_name = 'auto_roof'
urlpatterns = [
    path('', views.Auto_RoofList.as_view(), name='auto_roof_list'),
    path('add/', views.Auto_RoofCreate.as_view(), name='auto_roof_create'),
    path('<int:pk>/', views.Auto_RoofDetail.as_view(), name='auto_roof_detail'),
    path('<int:pk>/update/', views.Auto_RoofUpdate.as_view(), name='auto_roof_update'),
    path('<int:pk>/delete/', views.Auto_RoofDelete.as_view(), name='auto_roof_delete'),

    ## api
    path('api/auto_roof/', api.auto_roof_list_api, name='auto_roof_list_api'),
    path('api/auto_roof/<int:id>/', api.auto_roof_detail_api,
         name='auto_roof_detail_api'),

    ## class based view
    path('api/Auto_Roof/', api.Auto_Roof_list_Api.as_view(),
         name='Auto_Roof_list_Api'),
    path('api/Auto_Roof/<int:pk>/', api.Auto_Roof_detail_Api.as_view(),
         name='Auto_Roof_detail_Api'),

]
