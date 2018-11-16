"""gaddi URL Configuration

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

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from tube.views import EmployeeView
from rest_framework import routers

from tube.views import chart_view, chart1_view, simple_chart, index

router = routers.DefaultRouter()
router.register('Employees', EmployeeView)

urlpatterns = [
    path('bokeh1/', index),
    path('chart1/', chart1_view),
    path('bokeh/', simple_chart,  name= ""),
    path('chart/', chart_view),
    path('', include(router.urls)),
	path('jet/', include('jet.urls', 'jet')),
	path('jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')),
    path('admin/', admin.site.urls),
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)