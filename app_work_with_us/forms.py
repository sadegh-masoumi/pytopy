from django.core import validators
from django import forms
from django.core.exceptions import ValidationError
from django.core.files.uploadedfile import InMemoryUploadedFile


class WorkWithUsForm(forms.Form):
    fullName = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'نام خود را وارد کنید'}),
        validators=[validators.MaxLengthValidator(limit_value=30, message='نام شما بیشتراز 30 کاراکتر نمیتواند باشد')]
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'j.doe@example.com'}),
        validators=[
            validators.MaxLengthValidator(limit_value=80, message='ایمیل نمیتواند بیشتر از 80 کاراکتر باشد')
            , validators.EmailValidator(message='لطفا آدرس ایمیل معتبر وارد کنید.')
        ]
    )

    number = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control bg-image-0',
                                      'placeholder': '000-0000-00-00',
                                      'data-delimiter': '-',
                                      'data-blocks': '3 4 2 2',
                                      'data-format': 'custom',
                                      }),
        validators=[validators.MaxLengthValidator(limit_value=14,
                                                  message='تعداد کاراکتر شماره تماس نمیتواند بیشتر از 14 باشد.')]
    )

    description = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control', 'rows': '6', 'placeholder': 'متن شما'})

    )
    cv = forms.FileField(
        widget=forms.FileInput(attrs={'class': 'file-drop-input'}),
        required=False
    )

    def clean_cv(self):
        cv: InMemoryUploadedFile = self.cleaned_data.get('cv')
        if cv is not None:
            cv_name = cv.name.split('.')
            if cv_name[:-1] == 'JPG':
                pass
            else:
                raise ValidationError('شما فقط میتوانید عکس با فرمت های JPG آپلود کنید', code='فرمت فایل')
