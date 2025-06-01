from django.urls import path
from api import views

worker_urlpatterns = [
  path('worker/', views.WorkerView.as_view(), name='worker')
]