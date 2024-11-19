from django.urls import include, path
from django.views.generic import TemplateView
# from .views import CustomPasswordResetView, PasswordResetDoneView
from .views import  Register, CustomPasswordResetView
# from .views import login_view, reg_view

from django.contrib.auth import urls

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('register/', Register.as_view(), name="register"),

    # path('password_reset/', CustomPasswordResetView.as_view(), name='password_reset'),
    # path('password-reset/done/', PasswordResetDoneView.as_view(), name='password_reset_done'),
    # path('login/', login_view, name="login"),
    # path('reg/', reg_view, name="reg"),
]