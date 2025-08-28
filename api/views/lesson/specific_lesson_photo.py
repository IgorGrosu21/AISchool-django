from datetime import datetime
from drf_spectacular.utils import extend_schema
from django.shortcuts import get_object_or_404

from api.permissions import IsTeacher, IsKlassManager, CanEditSpecificLesson
from api.models import SpecificLesson, Lesson, Klass

from ..media import DetailedMediaView
    
@extend_schema(tags=['api / lesson'])
class SpecificLessonPhotosView(DetailedMediaView):
  permission_classes = [IsTeacher|IsKlassManager, CanEditSpecificLesson]
  container_field = 'specific_lesson'
  
  def get_lesson(self):
    klass: Klass = get_object_or_404(Klass, school__slug=self.kwargs.get('school_slug'), slug=self.kwargs.get('klass_slug'))
    return get_object_or_404(Lesson, klass__id=klass.id, id=self.kwargs.get('lesson_pk'))
  
  def get_date(self):
    return datetime.strptime(self.kwargs.get('date'), '%Y.%m.%d').date()
  
  def get_container(self):
    lesson = self.get_lesson()
    specific_lesson = get_object_or_404(SpecificLesson, lesson=lesson, date=self.get_date())
    self.check_object_permissions(self.request, specific_lesson)
    return specific_lesson