from django.urls import path
from django.conf.urls import url
from . import views , api


app_name = 'old_parts'
urlpatterns = [
    path('', views.Old_PartsList.as_view(), name='old_parts_list'),
    path('add/', views.Old_PartsCreate.as_view(), name='old_parts_create'),
    path('<int:pk>/', views.Old_PartsDetail.as_view(), name='old_parts_detail'),
    path('<int:pk>/update/', views.Old_PartsUpdate.as_view(),
         name='old_parts_update'),
    path('<int:pk>/delete/', views.Old_PartsDelete.as_view(),
         name='old_parts_delete'),

    ## api
    path('api/old_parts/', api.old_parts_list_api, name='old_parts_list_api'),
    path('api/old_parts/<int:id>/', api.old_parts_detail_api,
         name='old_parts_detail_api'),

    ## class based view
    path('api/Old_Parts/', api.Old_Parts_list_Api.as_view(),
         name='Old_Parts_list_Api'),
    path('api/Old_Parts/<int:pk>/', api.Old_Parts_detail_Api.as_view(),
         name='Old_Parts_detail_Api'),


]
