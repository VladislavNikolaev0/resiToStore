from lib2to3.fixes.fix_input import context

from django.contrib.auth import authenticate, login as user_login, logout as user_logout, login
from .forms import UserCreationForm
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .models import User
from django.views import View
from django.views.generic import TemplateView
from django.contrib.auth.views import PasswordResetView
from .forms import CustomPasswordResetForm

class Register(View):

    template_name = 'registration/register.html'

    def get(self, request):
        context = {
            'form' : UserCreationForm()
        }
        return render(request, self.template_name, context)

    def post(self, request):
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('assembling')

        context = {
            'form' : form
        }

        return render(request, self.template_name, context)

class CustomPasswordResetView(View):
    template_name = 'registration/password_reset_form.html'


class PasswordResetDoneView(TemplateView):
    template_name = 'password_reset_done.html'
# Create your views here.
# def login_view(request):
#
#     if request.method == 'POST':
#
#         login = request.POST.get('login')
#         password = request.POST.get('password')
#
#         user = authenticate(request, username=login, password=password)
#
#         if user is not None:
#             user_login(request, user)
#             return HttpResponseRedirect('/')
#         else:
#             return HttpResponseRedirect('/')
#
#     return render(request, 'users/login.html')
#
# def reg_view(request):
#
#     if request.method == 'POST':
#
#         login = request.POST.get('loginReg')
#         password = request.POST.get('passwordReg')
#         repeatPassword = request.POST.get('passwordRegRepeat')
#
#         if password == repeatPassword:
#
#             User.objects.create_user(login, password)
#
#             user = authenticate(request, username=login, password=password)
#
#             if user is not None:
#                 user_login(request, user)
#                 return HttpResponseRedirect('/')
#             else:
#                 return HttpResponseRedirect('/')
#
#     return render(request, 'users/reg.html')

# def login(request):
#     return render(request, 'users/login.html')