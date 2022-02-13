import random
import string

from .models import User
from .forms import RegisterForm, LoginForm, ForgetPasswordForm

from utils.email import EmailService

from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import Http404, JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse


def generate_token(count):
    letters = string.digits + string.ascii_letters
    return ''.join(random.choice(letters) for _ in range(count))


def login_user(request):
    if request.user.is_authenticated:
        return redirect(reverse('home'))

    login_form = LoginForm(request.POST or None)

    if login_form.is_valid():
        user = User.objects.get(email=login_form.cleaned_data.get('email'))
        print(user.is_active)
        user = authenticate(request, **login_form.cleaned_data)

        login(request, user)
        return redirect(reverse('home'))

    context = {
        'login_form': login_form,
    }
    return render(request, 'login.html', context)


def register_user(request):
    if request.user.is_authenticated:
        return redirect(reverse('home'))

    register_form = RegisterForm(request.POST or None)

    if register_form.is_valid():
        data = register_form.cleaned_data
        data.pop('re_password')
        user = User.objects.create_user(**data, is_active=False)
        token = generate_token(12)
        request.session['AuthorizationEmailCode'] = str(token)

        EmailService.send_email('تایید اکانت پای تو پای', [user.email], 'email/email_2.html',
                                {
                                    'url': f'https://pytopy.ir/verify-email/{user.pk}/{token}'
                                })
        return redirect(reverse('registered'))

    context = {
        'register_form': register_form
    }
    return render(request, 'register.html', context)


def registered(request):
    context = {
        'title': 'تایید ایمیل',
        'msg': 'اکانت شما با موفقیت ساخته شد. لطفا برای تایید ایمیل خود روی لینکی که به ایمیل شما فرستاده شده است '
               'کلیک کنید. '
    }
    return render(request, 'verify_email.html', context)


def verify_email(request, pk, token):
    if request.user.is_authenticated:
        return redirect(reverse('home'))

    user = get_object_or_404(User, id=pk)

    if user.is_active:
        raise Http404('شما قبلا ثبت نام کرده اید.')

    token = token
    valid_code = request.session.get('AuthorizationEmailCode', -1)

    if str(token) == valid_code:

        user.is_active = True
        user.save()
        login(request, user)

        del request.session['AuthorizationEmailCode']

        messages.success(request, 'ایمیل شما با موفقیت تایید شد. به پای تو پای خوش آمدید.')

        context = {
            'title': f'{user.username} خوش آمدید',
            'msg': 'شما وارد اکانت شده اید.'
        }
        return render(request, 'verify_email.html', context)
    else:
        raise Http404('لینک معتبر نمی باشد. لطفا دوباره تلاش کنید.')


@login_required(login_url="/login", redirect_field_name='')
def logout_user(request):
    logout(request)
    return redirect(reverse('home'))


def forget_password(request):
    if request.user.is_authenticated:
        return redirect(reverse('home'))

    form = ForgetPasswordForm(request.POST or None)

    if form.is_valid():
        token = generate_token(12)
        user = form.cleaned_data.get('email')

        request.session['AuthorizationEmailCode'] = str(token)
        EmailService.send_email('فراموشی رمز عبور', [user.email], 'email/email_2.html',
                                {
                                    'url': f'https://pytopy.ir/password-recovery/{user.pk}/{token}'
                                })
        context = {
            'title': ' تایید توسط ایمیل',
            'msg': 'برای شما یک ایمیل ارسال شد که در آن یک لینک می باشد با کلیک روی آن وارد اکانت خود شود و رمز خود '
                   'را تغییر دهید. '
        }
        return render(request, 'verify_email.html', context)
    context = {
        'form': form
    }
    return render(request, 'forget_password.html', context)


def password_recovery(request, pk, token):
    if request.user.is_authenticated:
        return redirect(reverse('home'))

    user = get_object_or_404(User, id=pk)

    token = token
    valid_code = request.session.get('AuthorizationEmailCode', -1)

    if str(token) == valid_code:
        login(request, user)

        del request.session['AuthorizationEmailCode']

        messages.success(request, 'ایمیل شما با موفقیت تایید شد. به پای تو پای خوش آمدید.')

        context = {
            'title': f'{user.username} خوش آمدید',
            'msg': 'شما وارد اکانت شده اید.'
        }

        return render(request, 'verify_email.html', context)

    else:
        raise Http404('لینک معتبر نمی باشد. لطفا دوباره تلاش کنید.')
