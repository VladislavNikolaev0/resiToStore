from django.urls import path, include
from . import views
from .views import *

urlpatterns = [
    path('', assembling, name='assembling'),
    path('popular', popular, name='popular'),
    path('instruction', instruction, name='instruction'),
    path('users/', include('users.urls')),
    path('processors/', processor_list, name='processor_list'),
    path('rams/', ram_list, name='ram_list'),
    path('motherbroads/', motherbroad_list, name='motherbroad_list'),
    path('powerUnits/', powerUnit_list, name='powerUnit_list'),
    path('cooler/', cooler_list, name='cooler_list'),
    path('corpus/', corpus_list, name='corpus_list'),
    path('videoCard/', videoCard_list, name='videoCard_list'),
    path('hdd/', hdd_list, name='hdd_list'),
    path('ssd/', ssd_list, name='ssd_list'),
]