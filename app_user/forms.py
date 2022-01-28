from django.core import validators

from django import forms
from .models import User


class RegisterForm(forms.Form):
    """
    register form for user by : username, email, number, password
    """
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control rounded', 'placeholder': 'نام کاربری'}))

    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': 'form-control rounded', 'placeholder': 'ایمیل'}))

    number = forms.IntegerField(
        widget=forms.TextInput(attrs={'class': 'form-control rounded', 'placeholder': 'موبایل'})
    )

    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'رمز عبور'}),
        validators=[validators.MinLengthValidator(limit_value=8, message='پسورد شما باید حداقل '
                                                                         '8 کاراکتر باشد')]
    )

    re_password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'تکرار رمز عبور'}),

    )

    def clean_email(self):
        email = self.cleaned_data.get('email')
        is_exists_user_by_username = User.objects.filter(email=email).exists()
        if is_exists_user_by_username:
            raise forms.ValidationError('آدرس ایمیل وارد شده قبلا استفاده شده است.')
        return email

    def clean_username(self):
        username = self.cleaned_data.get('username')
        is_exists_user_by_username = User.objects.filter(username=username).exists()
        if is_exists_user_by_username:
            raise forms.ValidationError('این نام کاربری قبلا استفاده شده است.')
        return username

    def clean_number(self):
        number = self.cleaned_data.get('number')
        if len(str(number)) > 11:
            raise forms.ValidationError('شماره تماس وارد شده معتبر نمی باشد')
        return number

    def clean_re_password(self):
        password = self.cleaned_data.get("password")
        re_password = self.cleaned_data.get("re_password")
        if password != re_password:
            raise forms.ValidationError('کلمه های عبور مغایرت دارند.')

        return password


class LoginForm(forms.Form):
    """
    login form by : email, password
    """
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={'class': 'form-control', 'placeholder': 'آدرس ایمیل'}
        )
    )

    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={'class': 'form-control', 'placeholder': 'رمز عبور'}
        )
    )

    def clean_email(self):
        email = self.cleaned_data.get("email")
        user = User.objects.filter(email=email).first()
        if user is None:
            raise forms.ValidationError('کاربری با این مشخصات یافت نشد')
        if user.is_active is False:
            raise forms.ValidationError(
                'کاربری با این مشخصات یافت نشد. لطفا ایمیل خود را از طریق لینک ارسال شده تایید کنید.')
        return email


class ForgetPasswordForm(forms.Form):
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={'class': 'form-control', 'placeholder': 'آدرس ایمیل'}
        )
    )

    def clean_email(self):
        email = self.cleaned_data.get("email")
        user = User.objects.filter(email=email).first()
        if user is None:
            raise forms.ValidationError('کاربری با این مشخصات یافت نشد')
        return user
