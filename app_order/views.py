import requests
import secrets
import string

from app_course.models import Course
from core.settings.base import DOWNLOAD_API, PYTOPY_TOKEN, MERCHANT_ID, DEBUG
from .models import Enroll
from .zarinpal import ZarinPal

from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.shortcuts import Http404, redirect
from django.contrib import messages


@login_required(login_url='/login')
def pay_request(request, course_id):
    course = get_object_or_404(Course, pk=course_id)

    enrolled = Enroll.objects.filter(user=request.user, course=course, is_pay=True)
    if enrolled.exists():
        Http404(
            'شما قبلا در این دوره ثبت نام کرده اید. اگر قصد دارید این دوره را دوباره تهیه کنید با یک اکانت دیگر لطفا '
            'تلاش کنید.')

    enroll, _ = Enroll.objects.get_or_create(user=request.user, course=course, is_pay=False,
                                             amount=course.get_final_price())
    if DEBUG:
        call_back_url = f"http://localhost:8000/pay-verify/{enroll.id}"
    else:
        call_back_url = f"https://pytopy.ir/pay-verify/{enroll.id}"

    pay = ZarinPal(merchant=MERCHANT_ID,
                   call_back_url=call_back_url)

    # email and mobile is optimal
    response = pay.send_request(amount=course.get_rial_price(),
                                description=f'ثبت نام و خرید دوره {course.name}',
                                email="pytopy.ir@gmail.com",
                                mobile='09359005490'
                                )
    if response.get('error_code') is None:
        # redirect object
        return response
    else:
        return HttpResponse(f'Error code: {response.get("error_code")}, Error Message: {response.get("message")}')


def pay_verify(request, enroll_id, *args, **kwargs):
    pay = ZarinPal(merchant=MERCHANT_ID)
    enroll = Enroll.objects.filter(id=enroll_id).first()

    if enroll is None:
        Http404('صفحه مورد نظر یافت نشد')

    response = pay.verify(request=request, amount=enroll.amount * 10)

    if response.get("transaction"):
        if response.get("pay"):
            alphabet = string.ascii_letters + string.digits
            token = ''.join(secrets.choice(alphabet) for i in range(20))
            data = {
                'client_token': token,
                'authorization': PYTOPY_TOKEN,
                'username': enroll.user.username,
            }
            requests.post(url=DOWNLOAD_API + 'create-client', data=data)

            enroll.is_pay = True
            enroll.token = token
            enroll.save()

            messages.success(request, 'شما با موفقیت  در دوره ثبت نام کرده اید. تبریک مطمئنم میترکونی :)')
            return redirect(enroll.course.get_absolute_url())
        else:
            messages.success(request, 'شما با موفقیت  در دوره ثبت نام کرده اید. تبریک مطمئنم میترکونی :)')
            return redirect(enroll.course.get_absolute_url())
    else:
        if response.get("status") == "ok":
            messages.error(request, f'{response.get("error_code") : response.get("message")}')
            return redirect(enroll.course.get_absolute_url())

        elif response.get("status") == "cancel":
            messages.error(request, 'تراکنش ناموفق بود لطفا دوباره تلاش کنید :)')
            return redirect(enroll.course.get_absolute_url())
