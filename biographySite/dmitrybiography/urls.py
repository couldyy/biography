from django.urls import path, include
from .views import *
from django.views.decorators.cache import cache_page


urlpatterns = [
    path('', home, name='home'),
    path('send-mail', send_email, name='send_mail')

]