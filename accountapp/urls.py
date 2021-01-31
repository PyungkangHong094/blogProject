from django.conf.urls import url
from django.contrib.auth.views import LoginView, LogoutView, PasswordResetView, PasswordResetDoneView, \
    PasswordResetConfirmView, PasswordResetCompleteView

from accountapp.forms import UserLoginForm
from accountapp.views import AccountCreateView, AccountDetailView, AccountUpdateView, AccountDeleteView
from django.urls import path, include
from django.contrib.auth import views as auth_views
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
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('password_reset/confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(),
         name='password_reset_confirm'),
    path('password_reset/complete/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]
