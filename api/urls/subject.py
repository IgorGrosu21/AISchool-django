from django.urls import path
from api import views

subject_urlpatterns = [
  path('subject-names/', views.SubjectNameListView.as_view(), name='subject-name-list'),
  path('subjects/', views.SubjectListView.as_view(), name='subject-list'),
]