from django.urls import path
from api.views import person as views

person_urlpatterns = [
  path('home/', views.PersonHomeView.as_view(), name='person-home'),
  path('parents/<uuid:pk>/', views.DetailedParentView.as_view(), name='parent-details'),
  path('students/<uuid:pk>/', views.DetailedStudentView.as_view(), name='student-details'),
  path('teachers/<uuid:pk>/', views.DetailedTeacherView.as_view(), name='teacher-details'),
]