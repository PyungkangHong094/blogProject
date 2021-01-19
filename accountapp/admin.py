from django.contrib import admin

from articleapp.models import Article

# Register your models here.
from commentapp.models import Comment
from profileapp.models import Profile
from projectapp.models import Project
from subscribeapp.models import Subscription

admin.site.register(Article)
admin.site.register(Comment)
admin.site.register(Profile)
admin.site.register(Project)
admin.site.register(Subscription)

