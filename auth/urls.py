from django.urls import path
from .views import SignUpView, LoginView, LogoutView, LogoutAllView, RefreshTokenView, SendVerificationEmailView, VerifyDetailedUserView, WorkerView

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('refresh/', RefreshTokenView.as_view(), name='refresh-token'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('logout-all/', LogoutAllView.as_view(), name='logout-all'),
    path('send-verification/', SendVerificationEmailView.as_view(), name='send-verification'),
    path('verify/', VerifyDetailedUserView.as_view(), name='verify'),
    path('worker/', WorkerView.as_view(), name='worker')
]