import random

from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from utils.email import EmailService
from .models import User
from django.http import Http404, JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from .forms import RegisterForm, LoginForm
from django.urls import reverse


def login_user(request):
    if request.user.is_authenticated:
        return redirect(reverse('home'))

    login_form = LoginForm(request.POST or None)

    if login_form.is_valid():
        user = authenticate(request, **login_form.cleaned_data)
        login(request, user)
        return redirect(reverse('home'))

    context = {
        'login_form': login_form,
    }
    return render(request, 'login.html', context)


def login_page(request):
    email = request.POST.get('email')
    password = request.POST.get('password')

    x = User.objects.filter(email=email).first()

    if x is None:
        response = JsonResponse({'mesg': 'کاربری با این مشخصات یافت نشد'})
        return response

    user = authenticate(request, username=x.username, email=email, password=password)

    if user is not None:
        user = User.objects.filter(user=user).first()
        login(request, user)
        return JsonResponse({'mesg': f'{user.username} خوش آمدید'})


def register_user(request):
    if request.user.is_authenticated:
        return redirect(reverse('home'))

    register_form = RegisterForm(request.POST or None)

    if register_form.is_valid():
        data = register_form.cleaned_data
        data.pop('re_password')
        User.objects.create_user(**data, is_active=False)

        return redirect(f'/verify-email')

    context = {
        'register_form': register_form
    }
    return render(request, 'register.html', context)


# def verify_email(request, user_id):
#     if request.user.is_authenticated:
#         return redirect("/")
#
#     user = get_object_or_404(User, id=user_id)
#     if user.is_active:
#         raise Http404('شما قبلا ثبت نام کرده اید.')
#
#     if request.method == "GET":
#         userInformation: UserInformation = UserInformation.objects.filter(user=user).first()
#         if userInformation is None:
#             raise Http404('مشخصات یافت نشد')
#
#         random_number = random.randint(100000, 999999)
#
#         userInformation.code = random_number
#         userInformation.save()
#         EmailService.send_email('تایید اکانت پای تو پای', ['sadegh.masoumi.ms@gmail.com'], 'email/email_1.html',
#                                 {
#                                     'code': random_number
#                                 })
#
#     if request.method == "POST":
#         code = request.POST.get('code')
#
#         userInformation: UserInformation = get_object_or_404(UserInformation, user=user)
#         if userInformation.code == code:
#             user.is_active = True
#             user.save()
#
#             login(request, user)
#             return redirect("/")
#         else:
#             raise Http404('کد وارد شده اشتباه می باشد')
#
#     context = {
#
#     }
#     return render(request, 'verify_email.html', context)


@login_required(login_url="/login", redirect_field_name='')
def logout_user(request):
    logout(request)
    return redirect(reverse('home'))
