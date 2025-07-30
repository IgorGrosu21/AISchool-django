from datetime import datetime
from rest_framework import generics, status
from rest_framework.views import Response, Request
from drf_spectacular.utils import extend_schema
from django.shortcuts import get_object_or_404

from api.permisions import IsStudentOrReadonly, CanEditHomework
from api.models import Student, Homework, SpecificLesson, Lesson, Klass
from api.serializers import DetailedHomeworkSerializer, StudentSerializer, SpecificLessonSerializer
    
@extend_schema(tags=['api / lesson'])
class DetailedHomeworkView(generics.RetrieveUpdateDestroyAPIView):
  permission_classes = [IsStudentOrReadonly, CanEditHomework]
  queryset = Homework.objects.all()
  serializer_class = DetailedHomeworkSerializer
  
  def get_lesson(self):
    klass = get_object_or_404(Klass, school=self.kwargs.get('school'), id=self.kwargs.get('klass'))
    return get_object_or_404(Lesson, klass=klass, id=self.kwargs.get('lesson'))
  
  def get_specific_lesson(self):
    return get_object_or_404(SpecificLesson, lesson=self.get_lesson(), id=self.kwargs.get('specific_lesson'))
  
  def get_student(self):
    return get_object_or_404(Student, id=self.kwargs.get('student'))
  
  def get_object(self):
    homework = None
    try:
      homework = Homework.objects.get(student=self.get_student(), specific_lesson=self.get_specific_lesson())
    finally:
      self.check_object_permissions(self.request, homework)
    return homework
  
  def get(self, request: Request, *args, **kwargs):
    instance = self.get_object()
    if instance:
      return self.retrieve(request, *args, **kwargs)
    student = self.get_student()
    specific_lesson = self.get_specific_lesson()
    data = {
      'id': '',
      'student': StudentSerializer(student).data,
      'comment': '',
      'links': '',
      'files': [],
      'last_modified': str(datetime.now()),
      'specific_lesson': SpecificLessonSerializer(specific_lesson).data
    }
    return Response(data, status=status.HTTP_200_OK)
  
  @extend_schema(exclude=True)
  def patch(self, request, *args, **kwargs):
    pass