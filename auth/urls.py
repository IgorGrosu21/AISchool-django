from django.urls import path
from . import views

urlpatterns = [
    path('refresh/', views.RefreshView.as_view()),
    path('signup/', views.SignUpView.as_view()),
    path('login/', views.LogInView.as_view()),
    path('restore/', views.RestoreView.as_view()),
    path('logout/', views.LogOutView.as_view()),
    path('logout_all/', views.LogOutAllView.as_view()),
    path('user/', views.UserView.as_view()),
]