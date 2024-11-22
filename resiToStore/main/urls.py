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
]