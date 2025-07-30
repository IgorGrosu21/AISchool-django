from django.urls import path
from api.views import manual as views

manual_urlpatterns = [
  path('manuals/', views.ManualListView.as_view(), name='manual-list'),
  path('manuals/<str:slug>/', views.DetailedManualView.as_view(), name='manual-details'),
  path('modules/<str:manual_slug>/<str:slug>/', views.DetailedModuleView.as_view(), name='module-details'),
  path('topics/<str:manual_slug>/<str:module_slug>/<str:slug>/', views.DetailedTopicView.as_view(), name='topic-details'),
  path('tasks/<str:manual_slug>/<str:module_slug>/<str:topic_slug>/<str:slug>/', views.DetailedTaskView.as_view(), name='task-details'),
]