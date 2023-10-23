# tajoura/urls.py

from django.urls import path
from .views import UserSignupView, LevelListView, LevelDetailView, UserLoginView,UserListView,UserMeView,SchoolListView,SchoolDetailView, BulkCreateSchoolsWithLevelsView

urlpatterns = [
    path('signup/', UserSignupView.as_view(), name='user-signup'),
    path('login/', UserLoginView.as_view(), name='user-login'),
    path('users/', UserListView.as_view(), name='user-list'),
    path('me/', UserMeView.as_view(), name='user-me'),
    path('schools/', SchoolListView.as_view(), name='school-list'),
    path('schools/<int:pk>/', SchoolDetailView.as_view(), name='school-detail'),
    
    path('levels/', LevelListView.as_view(), name='school-list'),
    path('levels/<int:pk>/', LevelDetailView.as_view(), name='school-detail'),

    # path('schools/bulk-create/', BulkCreateSchoolsWithLevelsView.as_view(), name='bulk-create-schools'),

]
