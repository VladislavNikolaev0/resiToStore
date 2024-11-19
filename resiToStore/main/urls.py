from django.urls import path, include
from . import views
from .views import assembling, popular, instruction

urlpatterns = [
    path('', assembling, name='assembling'),
    path('popular', popular, name='popular'),
    path('instruction', instruction, name='instruction'),
    path('users/', include('users.urls')),
]