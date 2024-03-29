"""pragmatic URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static  # 이미지를 가져오려면conf url를 가져와야함
from django.contrib import admin
from django.urls import path, include
import adminactions.actions as actions  # graph

import accountapp
import articleapp
import chatbotapp
from articleapp.views import ArticleListView

from django.contrib.auth import views as auth_views
# from accountapp.forms import ResetPasswordForm, NewPasswordForm


urlpatterns = [
    # path('grappelli/', include('grappelli.urls')),
    path('adminactions/', include('adminactions.urls')), # graph

    path('', ArticleListView.as_view(), name='home'),
    path('admin/', admin.site.urls),
    path('admin/', include('admin_honeypot.urls', namespace='admin_honeypot')),
    path('accounts/', include('accountapp.urls')),
    path('profiles/', include('profileapp.urls')),
    path('articles/', include('articleapp.urls')),
    path('comments/', include('commentapp.urls')),
    path('projects/', include('projectapp.urls')),
    path('subscribe/', include('subscribeapp.urls')),
    path('likes/', include('likeapp.urls')),
    path('chatbotapp/', include('chatbotapp.urls')),
    url(r'^info', articleapp.views.info, name='info'),
    url(r'^edits', accountapp.views.edits, name='edits'),
    url(r'^chathome', chatbotapp.views.chathome, name='chathome'),
    url(r'^announce', accountapp.views.announce, name='announce'),
    url(r'^homepage', articleapp.views.homepage, name='homepage'),

    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('password_reset/confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password_reset/complete/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),

    path("accounts/", include("allauth.urls")),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


actions.add_to_site(admin.site)