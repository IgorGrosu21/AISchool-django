from drf_spectacular.utils import extend_schema
from django.shortcuts import get_object_or_404

from api.permisions import IsStudent, CanEditHomework
from api.models import Student, Homework, SpecificLesson, Lesson, Klass

from ..media import DetailedMediaView

@extend_schema(tags=['api / lesson'])
class HomeworkPhotosView(DetailedMediaView):
  permission_classes = [IsStudent, CanEditHomework]
  container_field = 'homework'
  
  def get_lesson(self):
    klass = get_object_or_404(Klass, school=self.kwargs.get('school'), id=self.kwargs.get('klass'))
    return get_object_or_404(Lesson, klass=klass, id=self.kwargs.get('lesson'))
  
  def get_specific_lesson(self):
    return get_object_or_404(SpecificLesson, lesson=self.get_lesson(), id=self.kwargs.get('specific_lesson'))
  
  def get_student(self):
    return get_object_or_404(Student, id=self.kwargs.get('student'))
  
  def get_container(self):
    homework = get_object_or_404(Homework, student=self.get_student(), specific_lesson=self.get_specific_lesson())
    self.check_object_permissions(self.request, homework)
    return homework