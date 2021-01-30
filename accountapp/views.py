from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from django.http import HttpResponse, HttpResponseRedirect, HttpResponseForbidden
from django.shortcuts import render


# Create Your views here
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView
from django.views.generic.list import MultipleObjectMixin

from accountapp.decorators import account_ownership_required
from accountapp.forms import AccountUpdateForm, AccountCreateForm


# 배열로 만든다
from articleapp.models import Article

has_ownership = [account_ownership_required, login_required]

# @login_required
# def hello_world(request):
#     # 유저가 접속했는지 알아보는거
#     # if request.user.is_authenticated:
#     if request.method == "POST":
#
#         temp = request.POST.get('hello_world_input')
#
#         new_hello_world = HelloWorld()
#         new_hello_world.text = temp
#         new_hello_world.save()
#
#         # hello_world_list = HelloWorld.objects.all()
#         # 리프레쉬를 해도 돌아가지 않겠금 하는거
#         # 리버스틑 함수용
#         return HttpResponseRedirect(reverse('accountapp:hello_world'))
#     else:
#         hello_world_list = HelloWorld.objects.all()
#         return render(request, 'accountapp/hello_world.html', context={'hello_world_list': hello_world_list})
#     # else:
#     #     # 로그인이 안되어있을때 로그인창으로 리다이렉트리 보내준다
#     #     return HttpResponseRedirect(reverse('accountapp:login'))


class AccountCreateView(CreateView):
    model = User
    form_class = AccountCreateForm
    #리버스 레이지는 클래스에서만 사용한다
    success_url = reverse_lazy('articleapp:list')
    template_name = 'accountapp/create.html'

class AccountDetailView(DetailView, MultipleObjectMixin):
    model = User
    context_object_name = 'target_user'
    template_name = 'accountapp/detail.html'

    paginate_by = 10

    def get_context_data(self, **kwargs):
        object_list = Article.objects.all().filter(writer=self.get_object())

        return super(AccountDetailView, self).get_context_data(object_list=object_list, **kwargs)


    # def get(self, *args, **kwargs):
    #     if self.request.user.is_authenticated and self.get_object() == self.request.user:
    #         return super().get(*args, **kwargs)
    #     else:
    #         return HttpResponseForbidden()
    # def post(self, *args, **kwargs):
    #     if self.request.user.is_authenticated and self.get_object() == self.request.user:
    #         return super().post(*args, **kwargs)
    #     else:
    #         return HttpResponseForbidden()

@method_decorator(has_ownership, 'get')
@method_decorator(has_ownership, 'post')
class AccountUpdateView(UpdateView):
    model = User
    context_object_name = 'target_user'
    form_class = AccountUpdateForm
    success_url = reverse_lazy('articleapp:list')
    template_name = 'accountapp/update.html'

#     클래스 GET을 써주면 행동을 지정해줄수있다
#     def get(self, *args, **kwargs):
#         if self.request.user.is_authenticated and self.get_object() == self.request.user:
#             return super().get(*args, **kwargs)
#         else:
#             return HttpResponseForbidden()
#     def post(self, *args, **kwargs):
#         if self.request.user.is_authenticated and self.get_object() == self.request.user:
#             return super().post(*args, **kwargs)
#         else:
#             return HttpResponseForbidden()

@method_decorator(has_ownership, 'get')
@method_decorator(has_ownership, 'post')
class AccountDeleteView(DeleteView):
    model = User
    context_object_name = 'target_user'
    success_url = reverse_lazy('accountapp:login')
    template_name = 'accountapp/delete.html'

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated and self.get_object() == self.request.user:
            return super().get(*args, **kwargs)
        else:
            return HttpResponseForbidden()
    def post(self, *args, **kwargs):
        if self.request.user.is_authenticated and self.get_object() == self.request.user:
            return super().post(*args, **kwargs)
        else:
            return HttpResponseForbidden()

def edits(request):
    return render(request, 'accountapp/edits.html')
