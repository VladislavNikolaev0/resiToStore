from django.urls import path

from .views import assembling, popular, instruction

urlpatterns = [
    path('', assembling, name='assembling'),
    path('popular', popular, name='popular'),
    path('instruction', instruction, name='instruction')
]