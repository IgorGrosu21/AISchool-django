from django.urls import path
from api.views import subject as views

subject_urlpatterns = [
  path('subject-names/', views.SubjectNamesView.as_view(), name='subject-names'),
]