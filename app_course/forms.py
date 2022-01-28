from django.core import validators
from django import forms

from .models import STARS


class CourseCommentsForm(forms.Form):
    name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'نام خود را وارد کنید'}),
        validators=[validators.MaxLengthValidator(limit_value=30, message='نام شما بیشتراز 30 کاراکتر نمیتواند باشد')]
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'ایمیل'}),
        validators=[
            validators.MaxLengthValidator(limit_value=80, message='ایمیل نمیتواند بیشتر از 80 کاراکتر باشد')
            , validators.EmailValidator(message='لطفا آدرس ایمیل معتبر وارد کنید.')
        ]
    )

    description = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control', 'rows': '6', 'placeholder': 'متن شما'})
    )

    star = forms.ChoiceField(choices=STARS, widget=forms.Select(
        attrs={'class': 'form-select', 'placeholder': 'متن شما'}))
