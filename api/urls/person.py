from django.urls import path
from api import views

person_urlpatterns = [
  path('students/<uuid:pk>/', views.DetailedStudentView.as_view(), name='student-details'),
  path('teachers/<uuid:pk>/', views.DetailedTeacherView.as_view(), name='teacher-details'),
]