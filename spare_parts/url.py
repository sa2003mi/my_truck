from django.urls import path
from django.conf.urls import url
from . import views ,api


app_name = 'spare_parts'
urlpatterns = [
    path('', views.Spare_PartsList.as_view(), name='spare_parts_list'),
    path('add/', views.Spare_PartsCreate.as_view(), name='spare_parts_create'),
    path('<int:pk>/', views.Spare_PartsDetail.as_view(), name='spare_parts_detail'),
    path('<int:pk>/update/', views.Spare_PartsUpdate.as_view(), name='spare_parts_update'),
    path('<int:pk>/delete/', views.Spare_PartsDelete.as_view(), name='spare_parts_delete'),

    ## api
    path('api/spare_parts/', api.spare_parts_list_api, name='spare_parts_list_api'),
    path('api/spare_parts/<int:id>/', api.spare_parts_detail_api,
         name='spare_parts_detail_api'),

    ## class based view
    path('api/Spare_Parts/', api.Spare_Parts_list_Api.as_view(),
         name='Spare_Parts_list_Api'),
    path('api/Spare_Parts/<int:pk>/', api.Spare_Parts_detail_Api.as_view(),
         name='Spare_Parts_detail_Api'),


]
