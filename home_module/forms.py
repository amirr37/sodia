from django import forms
from .models import Post


class UserForm(forms.Form):
    first_name = forms.CharField(max_length=50, label='نام',
                                 error_messages={'required': 'لطفا نام خود را وارد کنید',
                                                 'max_length': 'نام نمیتواند بیشتر از ۵۰ کاراکتر باشد'},
                                 widget=forms.TextInput(attrs={
                                     'class': 'single-field',
                                     'placeholder': 'نام'

                                 }))

    last_name = forms.CharField(label='نام خانوادگی', max_length=50,
                                error_messages={'required': 'لطفا نام خود را وارد کنید',
                                                'max_length': 'نام خانوادگی نمیتواند بیشتر از ۵۰ کاراکتر باشد'},
                                widget=forms.TextInput(attrs={
                                    'class': 'single-field',
                                    'placeholder': 'نام خانوادگی'

                                }))
    username = forms.CharField(label='نام کاربری', max_length=50,
                               error_messages={'required': 'لطفا نام کاربری خود را وارد کنید',
                                               'max_length': 'نام کاربری نمیتواند بیشتر از ۵۰ کاراکتر باشد'},
                               widget=forms.TextInput(attrs={
                                   'class': 'single-field',
                                   'placeholder': 'نام کاربری'

                               }))
    email = forms.EmailField(label='ایمیل', widget=forms.EmailInput(
        attrs={
            'class': 'single-field',
            'placeholder': 'ایمیل'
        }
    )
                             )
    password = forms.CharField(label='رمز عبور', max_length=50,
                               error_messages={'required': 'لطفا رمز عبور خود را وارد کنید',
                                               'max_length': 'رمز عبور نمیتواند بیشتر از ۵۰ کاراکتر باشد'},
                               widget=forms.TextInput(attrs={
                                   'class': 'single-field',
                                   'placeholder': 'رمز عبور'

                               }))


class LoginForm(forms.Form):
    username = forms.CharField(max_length=50, label='نام کاربری',
                               error_messages={'required': 'لطفا نام  کاربری خود را وارد کنید',
                                               'max_length': 'نام کاربری نمیتواند بیشتر از ۵۰ کاراکتر باشد'},
                               widget=forms.TextInput(attrs={
                                   'class': 'single-field',
                                   'placeholder': 'نام کاربری'

                               }))
    password = forms.CharField(max_length=50, label='رمز عبور',
                               error_messages={'required': 'لطفا رمز عبور خود را وارد کنید',
                                               'max_length': 'رمز عبور نمیتواند بیشتر از ۵۰ کاراکتر باشد'},
                               widget=forms.TextInput(attrs={
                                   'class': 'single-field',
                                   'placeholder': 'رمز عبور'

                               }))


