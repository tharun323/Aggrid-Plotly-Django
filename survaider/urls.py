from django.conf.urls import url, include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from . views import AdultdataViewSet
from . import views
router = routers.DefaultRouter()

router.register(r'Adultsdata', views.AdultdataViewSet, base_name='Adultdataviewset')

urlpatterns = [
    url('api/', include(router.urls)),
    url('datatable',views.datatable,name='datatable'),
    url('charts',views.charts,name='charts')
]



