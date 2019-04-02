"""gwtauth URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from allauth.account.views import confirm_email
from django.urls.conf import re_path
from django.views.generic.base import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/v1/', include('api.urls'),name='api'),
    path('accounts/', include('allauth.urls')),
    path('accounts/profile/', RedirectView.as_view(url='/', permanent=True), name='profile-redirect'),
    path('auth/', include('rest_auth.urls')),
    re_path(r'auth/registration/account-confirm-email/(?P<key>[-:\w]+)/$', confirm_email, name='account_confirm_email'),
    path('auth/registration/', include('rest_auth.registration.urls')),
]
urlpatterns += static(settings.INFO_URL, document_root=settings.INFO_ROOT)
