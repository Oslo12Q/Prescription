from django.conf.urls import  include, url
from . import views

from rest_framework import routers
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^list_prescription/',views.PrescriptionList.as_view()),
    url(r'^detail/(?P<pk>[0-9]+)$',views.prescriptionDetail.as_view()),
    url(r'^dev/$',views.dev,name='dev'),
]
urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
