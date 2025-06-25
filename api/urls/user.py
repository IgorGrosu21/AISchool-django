from django.urls import path
from api import views

user_urlpatterns = [
  path('user/', views.DetailedUserView.as_view(), name='user-details'),
  path('user-routes/', views.UserRoutesView.as_view(), name='user-routes'),
]