"""adelportfolio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path, include
from portfolio import views
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('blog/', include('blog.urls')),
    path('projects/', views.adelprojects, name='projects'),
    path('contact/', views.contact, name='contact'),
    path('thanks/', views.thanks, name='thanks'),
    path('certificates/', views.adelcertificates, name='certificates'),
    path('django', views.django, name='django'),
    path('python', views.python, name='python'),
    path('ai', views.ai, name='ai'),
    path('digitalmarketing', views.digitalmarketing, name='digitalmarketing'),
    path('api', views.api, name='api'),
    path('certificates/<int:certificate_id>', views.detail, name='detail'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
