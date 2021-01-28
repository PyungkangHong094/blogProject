from django.contrib.auth.views import LoginView, LogoutView

from accountapp.forms import UserLoginForm
from accountapp.views import AccountCreateView, AccountDetailView, AccountUpdateView, AccountDeleteView
from django.urls import path, include

app_name = "accountapp"

urlpatterns = [


    path('login/', LoginView.as_view(template_name='accountapp/login.html', authentication_form=UserLoginForm), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),

    path('create/', AccountCreateView.as_view(), name='create'),
    path('detail/<int:pk>', AccountDetailView.as_view(), name='detail'),
    path('update/<int:pk>', AccountUpdateView.as_view(), name='update'),
    path('delete/<int:pk>', AccountDeleteView.as_view(), name='delete'),
    path('settings/<int:pk>', AccountDetailView.as_view(), name='settings'),
]
