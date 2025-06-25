from django.urls import path
from api import views

subject_urlpatterns = [
  path('subject-names/', views.SubjectNameListView.as_view(), name='subject-name-list'),
  path('subjects/', views.SubjectListView.as_view(), name='subject-list'),
  path('subjects/<str:slug>/', views.DetailedSubjectView.as_view(), name='subject-details'),
  path('subjects/<str:subject_slug>/<str:slug>/', views.DetailedModuleView.as_view(), name='module-details'),
  path('subjects/<str:subject_slug>/<str:module_slug>/<str:slug>/', views.DetailedTopicView.as_view(), name='topic-details'),
  path('subjects/<str:subject_slug>/<str:module_slug>/<str:topic_slug>/theories/<str:slug>/', views.DetailedTheoryView.as_view(), name='theory-details'),
  path('subjects/<str:subject_slug>/<str:module_slug>/<str:topic_slug>/tasks/<str:slug>/', views.DetailedTaskView.as_view(), name='task-details'),
]