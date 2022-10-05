from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render, redirect
from django.views.generic import CreateView, TemplateView

import string
import random

from short_url.settings import ALLOWED_HOSTS
from .forms import UrlShortForm
from .models import UrlService


class UserLogIn(LoginView):
    template_name = 'login.html'
    next_page = 'url_short/'


class UserRegistration(CreateView):
    model = User
    form_class = UserCreationForm
    template_name = 'registration.html'
    success_url = '/reg_done/'


class UserRegDone(TemplateView):
    template_name = 'reg_done.html'


class UserLogOut(LogoutView):
    template_name = 'logout.html'

#Скорректировать код по  аналогии с Артемом
@login_required
def url_short(request):
    if request.method == 'POST':
        form = UrlShortForm(request.POST)
        user = User.objects.get(username=request.user.username)
        if form.is_valid():
            url_all = form.cleaned_data["url_all"]
            if (r'http://' not in url_all) and (r"https://" not in url_all):
                url_all = r'http://' + url_all
            if UrlService.objects.filter(url_all=url_all,username_id=user.pk).exists():
                data = UrlService.objects.get(url_all=url_all)
                url_shorted = data.url_short
            else:
                url_shorted = ''.join([random.choice(string.ascii_letters + string.digits) for _ in range(10)])
                url_shorted = r'http://127.0.0.1:8000/sh/' + url_shorted
                new_url = UrlService(url_all=url_all, url_short=url_shorted, username_id=user.pk)
                new_url.save()
            context_short = {'url_all': url_all,
                             'url_shorted': url_shorted,
                             'form': UrlShortForm()}
            return render(request, 'short_url.html', context_short)
    else:
        form = UrlShortForm()
        context = {'form': form}
        return render(request, 'short_url.html', context)


@login_required
def list_url_short(request):
    name = User.objects.get(username=request.user.username)
    url = UrlService.objects.filter(username_id=name)
    context = {'name': name, 'url': url}
    return render(request, 'list_short_url.html', context)


def url_redirect(request, short):
    # fan = ALLOWED_HOSTS[0]
    # data = UrlService.objects.get(url_short=f'{fan}:8000/sh/{short}')
    data = UrlService.objects.get(url_short=f'http://127.0.0.1:8000/sh/{short}')
    return redirect(data.url_all)
#Скорректировать  пл константу Хоста