from django.contrib import admin


# Register your models here.
# from accountapp.models import Acount
from articleapp.models import Article
from commentapp.models import Comment
from profileapp.models import Profile
from projectapp.models import Project
from subscribeapp.models import Subscription

class DisplayAritcle(admin.ModelAdmin):
    list_display = ('writer', 'title', 'project', 'image', 'content', 'content', 'created_at')
    search_fields = ['title']
admin.site.register(Article, DisplayAritcle)

class DisplayComment(admin.ModelAdmin):
    list_display = ('writer', 'article', 'content', 'created_at')
    search_fields = ['content']
admin.site.register(Comment, DisplayComment)


admin.site.register(Profile)
admin.site.register(Project)
admin.site.register(Subscription)

