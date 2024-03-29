from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView, ListView
from django.views.generic.edit import FormMixin

from articleapp.decorators import article_ownership_required
from articleapp.forms import ArticleCreationForm
from articleapp.models import Article
from commentapp.forms import CommentCreationForm

from django.utils import timezone, dateformat

@method_decorator(login_required,'get')
@method_decorator(login_required,'post')
class ArticleCreateView(CreateView):
    model = Article
    form_class = ArticleCreationForm

    template_name = 'articleapp/create.html'

    def form_valid(self, form):
        temp_article = form.save(commit=False)
        temp_article.writer = self.request.user
        temp_article.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('articleapp:detail', kwargs={'pk': self.object.pk})



class ArticleDetailView(DetailView, FormMixin):
    model = Article
    form_class = CommentCreationForm
    context_object_name = 'target_article'
    formatted_date = dateformat.format(timezone.now(), 'Y-m-d H:i:s')
    template_name = 'articleapp/detail.html'



    # def get_context_data(self, **kwargs):
    #     context = super(ArticleDetailView, self).get_context_data(**kwargs)
    #     slug = self.kwargs['pk']
    #
    #     post = Article.objects.get(pk=slug)
    #
    #     next_page = Article.objects.filter(pk__gt=post.pk).exists()
    #     pre_page = Article.objects.filter(pk__lt=post.pk).exists()
    #
    #     if next_page:
    #         context['has_next_page'] = True
    #         context['next_page'] = Article.objects.filter(
    #             pk__gt=post.pk).first()
    #
    #     if pre_page:
    #         context['has_pre_page'] = True
    #         context['pre_page'] = Article.objects.filter(
    #             pk__lt=post.pk).order_by('-pk').first()

@method_decorator(article_ownership_required,'get')
@method_decorator(article_ownership_required,'post')
class ArticleUpdateView(UpdateView):
    model = Article
    context_object_name = 'target_article'
    form_class = ArticleCreationForm
    template_name = 'articleapp/update.html'


    def get_success_url(self):
        return reverse('articleapp:detail', kwargs={'pk': self.object.pk})


@method_decorator(article_ownership_required,'get')
@method_decorator(article_ownership_required,'post')
class ArticleDeleteView(DeleteView):
    model = Article
    context_object_name = 'target_article'
    success_url = reverse_lazy('articleapp:list')
    template_name = 'articleapp/delete.html'



class ArticleListView(ListView):
    model = Article
    context_object_name = 'article_list'
    template_name = 'articleapp/list.html'
    ordering = ['-pk']
    paginate_by = 40




def info(request):
    return render(request, 'articleapp/info.html')

def homepage(request):
    return render(request, 'articleapp/homepage.html')
