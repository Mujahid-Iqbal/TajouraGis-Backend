# tajoura/urls.py

from django.urls import path
from .views import UserSignupView, UserLoginView,UserListView,UserMeView

urlpatterns = [
    path('signup/', UserSignupView.as_view(), name='user-signup'),
    path('login/', UserLoginView.as_view(), name='user-login'),
    path('users/', UserListView.as_view(), name='user-list'),
    path('me/', UserMeView.as_view(), name='user-me'),
]
