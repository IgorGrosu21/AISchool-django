from datetime import datetime
from drf_spectacular.utils import extend_schema
from django.shortcuts import get_object_or_404

from api.permisions import IsTeacher, IsKlassManager, CanEditSpecificLesson
from api.models import SpecificLesson, Lesson, Klass

from ..media import DetailedMediaView
    
@extend_schema(tags=['api / lesson'])
class SpecificLessonPhotosView(DetailedMediaView):
  permission_classes = [IsTeacher, IsKlassManager, CanEditSpecificLesson]
  container_field = 'specific_lesson'
  
  def get_lesson(self):
    klass = get_object_or_404(Klass, school=self.kwargs.get('school'), id=self.kwargs.get('klass'))
    return get_object_or_404(Lesson, klass=klass, id=self.kwargs.get('lesson'))
  
  def get_date(self):
    return datetime.strptime(self.kwargs.get('date'), '%Y.%m.%d').date()
  
  def get_container(self):
    specific_lesson = get_object_or_404(SpecificLesson, lesson=self.get_lesson(), date=self.get_date())
    self.check_object_permissions(self.request, specific_lesson)
    return specific_lesson