"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path ,include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns
urlpatterns = i18n_patterns(
    path('admin/', admin.site.urls),
    path('', include('service.url' , namespace='service')),
    path('mechanic/', include('mechanic.url', namespace='mechanic')),
    path('driver/', include('driver.url', namespace='driver')),
    path('auto_roof/', include('auto_roof.url', namespace='auto_roof')),
    path('spare_parts/', include('spare_parts.url', namespace='spare_parts')),
    path('old_parts/', include('old_parts.url', namespace='old_parts')),
    path('accounts/', include('accounts.url', namespace='accounts')),
    path('contact/', include('contact.url', namespace='contact')),
    path('api-auth/', include('rest_framework.urls')),
)

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
