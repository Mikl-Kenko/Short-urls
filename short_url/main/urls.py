from django.urls import path, include

from .views import UserLogIn, UserRegistration, UserRegDone, url_short, list_url_short, url_redirect, UserLogOut

app_name = 'main'

urlpatterns = [
    path('', UserLogIn.as_view(), name='login'),
    path('reg/', UserRegistration.as_view(), name='reg'),
    path('reg_done/', UserRegDone.as_view(), name='reg_done'),
    path('log_out', UserLogOut.as_view(), name='log_out'),
    path('url_short/', url_short, name='url_short'),
    path('list_short_url/', list_url_short, name='list_url_short'),
    path('sh/<str:short>', url_redirect, name='url_redirect'),
]
