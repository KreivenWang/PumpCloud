# _*_ encoding:utf-8 _*_

"""testproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic import TemplateView

from pump.views import CompanyView,loadFailureList,PumpListView,PumpView
from spectrum.views import FaultListView,FaultView,SpectrumView

import xadmin
# xadmin.autodiscover()
# from xadmin.plugins import xversion
# xversion.register_models()
# urlpatterns = [
#     url(r'^xadmin/', xadmin.site.urls),
# ]
urlpatterns = [
    url(r'^xadmin/', xadmin.site.urls,name="xadmin"),
    url('^$', CompanyView.as_view(), name="index"),
    url('^loadFailureList/$', loadFailureList.as_view(), name="loadFailureList"),
    url('^pumpList/$',PumpListView.as_view(), name="pumpList"),
    url('^faultList/$',FaultListView.as_view(), name="faultList"),

    url('^pump/$',PumpView.as_view(), name="pump"),
    # url('^fault/(?P<id>\d+)/$',FaultView.as_view(), name="fault"),
    url('^spectrum/(?P<id>\d+)/$',SpectrumView.as_view(), name="spectrum"),
]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
