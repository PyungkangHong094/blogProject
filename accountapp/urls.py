from django.contrib.auth.views import LoginView, LogoutView, PasswordResetView, PasswordResetDoneView, \
    PasswordResetConfirmView, PasswordResetCompleteView

from accountapp.forms import UserLoginForm
from accountapp.views import AccountCreateView, AccountDetailView, AccountUpdateView, AccountDeleteView
from django.urls import path, include

from accountapp.forms import ResetPasswordForm, NewPasswordForm


app_name = "accountapp"

urlpatterns = [


    path('login/', LoginView.as_view(template_name='accountapp/login.html', authentication_form=UserLoginForm), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),

    path('create/', AccountCreateView.as_view(), name='create'),
    path('detail/<int:pk>', AccountDetailView.as_view(), name='detail'),
    path('update/<int:pk>', AccountUpdateView.as_view(), name='update'),
    path('delete/<int:pk>', AccountDeleteView.as_view(), name='delete'),
    path('settings/<int:pk>', AccountDetailView.as_view(), name='settings'),
    path('password-reset/',
         PasswordResetView.as_view(template_name="accountapp/reset_password.html",form_class=ResetPasswordForm),
         name="password_reset"),

    path('password-reset/done/',
       PasswordResetDoneView.as_view(template_name="accountapp/reset_password_done.html"),
       name="password_reset_done"),

    path('password-reset-confirm/<uidb64>/<token>/',
       PasswordResetConfirmView.as_view(template_name="accountapp/reset_password_confirm.html",form_class=NewPasswordForm),
       name="password_reset_confirm"),

    path('password-reset-complete/',
       PasswordResetCompleteView.as_view(template_name="accountapp/reset_password_complete.html"),
       name="password_reset_complete"),
]
