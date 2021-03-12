from django.contrib import admin


# Register your models here.
# from accountapp.models import Acount
from articleapp.models import Article
from commentapp.models import Comment
from profileapp.models import Profile
from projectapp.models import Project
from subscribeapp.models import Subscription


# 관리자창에 필터 효과를 넣은 것들
class DisplayAritcle(admin.ModelAdmin):
    list_display = ('writer', 'title', 'project', 'image', 'content', 'content', 'created_at')
    search_fields = ['title']
    list_filter = ['project']


admin.site.register(Article, DisplayAritcle)


class DisplayComment(admin.ModelAdmin):
    list_display = ('writer', 'article', 'content', 'created_at')
    search_fields = ['content']
    list_filter = ['article']


admin.site.register(Comment, DisplayComment)


class DisplayProfile(admin.ModelAdmin):
    list_display = ('user', 'nickname', 'image', 'message')
    search_fields = ['nickname']
    list_filter = ['nickname']


admin.site.register(Profile, DisplayProfile)


class DisplayProject(admin.ModelAdmin):
    list_display = ('writer','title', 'description', 'created_at')
    search_fields = ['title']
    list_filter = ['title']


admin.site.register(Project, DisplayProject)


class DisplaySub(admin.ModelAdmin):
    list_display = ('user', 'project')
    search_fields = ['project']
    list_filter = ['project']


admin.site.register(Subscription, DisplaySub)

