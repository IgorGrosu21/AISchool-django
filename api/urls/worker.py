from django.urls import path
from api.views import worker as views

worker_urlpatterns = [
  path('worker/', views.WorkerView.as_view(), name='worker')
]