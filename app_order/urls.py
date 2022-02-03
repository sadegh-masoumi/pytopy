from django.urls import path
from .views import pay_request, pay_verify

urlpatterns = [

    path('pay-request/<int:course_id>', pay_request, name='pay-request'),
    path('pay-verify/<int:enroll_id>', pay_verify, name='pay-verify')
]
