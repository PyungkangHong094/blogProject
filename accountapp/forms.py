from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordResetForm, SetPasswordForm
from django import forms

# 서버에 보내도 서버에 반영되지않는다.

class UserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)

    username = forms.CharField(widget=forms.TextInput(attrs={
        "class": "input",
        "type": "text",
        "placeholder": "아이디"
    }))

    password = forms.CharField(widget=forms.TextInput(attrs={
        "class": "input",
        "type": "password",
        "placeholder": "패스워드"
    }))


class AccountUpdateForm(UserCreationForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['username'].disabled = True


class AccountCreateForm(UserCreationForm):

    def __init__(self, *args, **kwargs):
        
        super().__init__(*args, **kwargs)


        self.fields['username'].label = "아이디 "
        self.fields['username'].help_text = "필수: 영문, 숫자 및 특수문자 @/./+/-/_ 사용가능 150자 이내 "
        self.fields['email'].label = "이메일 주소"
        self.fields['password1'].label = "비밀번호"
        self.fields['password1'].help_text = "<ul><li>" \
        "아이디와 유사도가 높을 경우 사용이 불가합니다.</li>" \
        "<li>비밀번호는 최소 8글자 이상이어야 합니다.</li>" \
        "<li>너무 흔한 비밀번호는 사용이 불가합니다.</li>" \
        "<li>숫자만으로 구성된 비밀번호는 사용이 불가합니다." \
        "</li></ul>"
        self.fields['password2'].label = "비밀번호 확인"
        self.fields['password2'].help_text = "입력하신 비밀번호를 다시 입력해주세요."

    class Meta:
        fields = ['username','email','password1', 'password2']
        model = get_user_model()


class ResetPasswordForm(PasswordResetForm):
    def __init__(self, *args, **kwargs):
        super(ResetPasswordForm, self).__init__(*args, **kwargs)

    email = forms.CharField(widget=forms.TextInput(attrs={
        "class": "input",
        "type": "email",
        "placeholder": "enter email-id"
    }))


class NewPasswordForm(SetPasswordForm):
    def __init__(self, *args, **kwargs):
        super(NewPasswordForm, self).__init__(*args, **kwargs)

    new_password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': "input",
            "type": "password",
            'autocomplete': 'new-password'
        }))

    new_password2 = forms.CharField(
        strip=False,
        widget=forms.PasswordInput(attrs={
            'class': "input",
            "type": "password",
            'autocomplete': 'new-password'
        }))


class UserRegistrationForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        "class": "input",
        "type": "text",
        "placeholder": "enter username"
    }))

    email = forms.CharField(widget=forms.TextInput(attrs={
        "class": "input",
        "type": "email",
        "placeholder": "enter email-id"
    }))

    password1 = forms.CharField(widget=forms.TextInput(attrs={
        "class": "input",
        "type": "password",
        "placeholder": "enter password"
    }))

    password2 = forms.CharField(widget=forms.TextInput(attrs={
        "class": "input",
        "type": "password",
        "placeholder": "re-enter password"
    }))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', "password2"]