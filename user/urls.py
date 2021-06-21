from django.urls import path
from user.views import sign_in, sign_up

urlpatterns = [
    path('signin', sign_in, name='sign_in'),
    path('signup', sign_up, name='sign_up'),
]
