from django.urls import path
from api import views

user_urlpatterns = [
  path('user/', views.UserView.as_view(), name='user'),
]