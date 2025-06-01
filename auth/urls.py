from django.urls import path
from .views import SignUpView, LoginView, LogoutView, LogoutAllView, RefreshTokenView, WorkerView

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('logout-all/', LogoutAllView.as_view(), name='logout_all'),
    path('refresh/', RefreshTokenView.as_view(), name='refresh_token'),
    path('worker/', WorkerView.as_view(), name='worker')
]