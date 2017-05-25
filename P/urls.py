from django.conf.urls import  include, url
from . import views


from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^list_prescription/$',views.list_prescription,name = 'list_prescription'),
    url(r'^list_ption/$',views.list_only,name = 'list_only'),
#    url(r'^increase_ption/$',views.increase_ption,name = 'increase_ption'),
    url(r'^update_ption/$',views.update_ption,name = 'update_ption'),
    url(r'^dev/$',views.dev,name='dev'),
]
urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
