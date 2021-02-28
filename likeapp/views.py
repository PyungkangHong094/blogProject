from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views.generic import RedirectView

from articleapp.models import Article
from likeapp.models import LikeRecord


@method_decorator(login_required, 'get')
class LikeArticleView(RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        return reverse('articleapp:detail', kwargs={'pk': kwargs['pk']})

    #
    def get(self, *args, **kwargs):
        # 원하는 알고리즘
        # 유저는 자기자신을 리퀘스트는 보내는 유저
        user = self.request.user
        # 아티클은 그 PK를 받은 값이 가져오면 가져오는거고 만약 없으면 404 에러를 보내준다
        article = get_object_or_404(Article, pk=kwargs['pk'])

        # 이사람이 이 게시글에 좋아요를 눌렀는지 확인과정
        # 유저가 저희가 찾은 유저 , 아티클은 저희가 방금 찾아놓은 아티클,
        if LikeRecord.objects.filter(user=user, article=article).exists():
            return HttpResponseRedirect(reverse('articleapp:detail', kwargs={'pk': kwargs['pk']}))
        else:
            LikeRecord(user=user, article=article).save()

        article.like += 1
        article.save()

        return super(LikeArticleView, self).get(self.request, *args, **kwargs)
    # 유저가 로그인을해야지 좋아요를 할수있게