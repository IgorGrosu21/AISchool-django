from django.urls import path
from api.views import user as views

user_urlpatterns = [
  path('user/', views.DetailedUserView.as_view(), name='user-details'),
  path('user-routes/', views.UserRoutesView.as_view(), name='user-routes'),
]