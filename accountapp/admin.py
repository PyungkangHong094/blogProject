from django.contrib import admin
from rangefilter.filter import DateRangeFilter, DateTimeRangeFilter
from django.utils.safestring import mark_safe

# Register your models here.
# from accountapp.models import Acount
from articleapp.models import Article
from commentapp.models import Comment
from profileapp.models import Profile
from projectapp.models import Project
from subscribeapp.models import Subscription


# 관리자창에 필터 효과를 넣은 것들
class DisplayArticle(admin.ModelAdmin):
    list_display = ('writer', 'title', 'project', 'image', 'content', 'like', 'created_at')
    search_fields = ['title']
    list_filter = ('project', ('created_at', DateTimeRangeFilter))  # 튜플로도 가능하다
    ordering = ['created_at']
    readonly_fields = ['writer', 'like']

    # 추가를 삭제해준거
    def has_add_permission(self, request):
        return False

    # 삭제를 못하게 하는거
    def has_delete_permission(self, request, obj=None):
        return False

    def get_image(self, obj):
        return mark_safe('<img src="{ url }" width="{ width }" height={ height } />'.format(
            url=obj.image.url,
            width=200,
            height=200,
        ))


admin.site.register(Article, DisplayArticle)


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

