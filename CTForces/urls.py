"""CTForces URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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

import debug_toolbar
from django.conf import settings
from django.conf.urls import include
from django.urls import path, re_path
from django.views.generic import RedirectView

from website.admin import custom_admin_site

urlpatterns = [
    path('admin/', custom_admin_site.urls),

    re_path('^favicon\.ico$',
            RedirectView.as_view(url=settings.FAVICON_PATH, permanent=True)),

    re_path('^apple-touch-icon\.png$',
            RedirectView.as_view(url=settings.APPLE_TOUCH_ICON_PATH, permanent=True)),

    re_path('^apple-touch-icon-precomposed\.png$',
            RedirectView.as_view(url=settings.APPLE_TOUCH_ICON_PRECOMPOSED_PATH, permanent=True)),

    re_path('^', include('website.urls')),
]

if settings.DEBUG:
    urlpatterns = [
                      re_path(r'^__debug__/', include(debug_toolbar.urls)),
                  ] + urlpatterns

urlpatterns += [re_path('^silk/', include('silk.urls', namespace='silk'))]
