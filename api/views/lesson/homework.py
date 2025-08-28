from datetime import datetime
from rest_framework import generics, status, mixins
from rest_framework.views import Response, Request
from drf_spectacular.utils import extend_schema
from django.shortcuts import get_object_or_404

from api.permissions import IsStudentOrReadonly, CanEditHomework
from api.models import Student, Homework, SpecificLesson, Lesson, Klass
from api.serializers import DetailedHomeworkSerializer, StudentSerializer, SpecificLessonSerializer, NoteNameSerializer
    
@extend_schema(tags=['api / lesson'])
class DetailedHomeworkView(generics.RetrieveUpdateDestroyAPIView, mixins.CreateModelMixin):
  permission_classes = [IsStudentOrReadonly, CanEditHomework]
  queryset = Homework.objects.all()
  serializer_class = DetailedHomeworkSerializer
  
  def get_lesson(self):
    klass: Klass = get_object_or_404(Klass, school__slug=self.kwargs.get('school_slug'), slug=self.kwargs.get('klass_slug'))
    return get_object_or_404(Lesson, klass__id=klass.id, id=self.kwargs.get('lesson_pk'))
  
  def get_specific_lesson(self):
    return get_object_or_404(SpecificLesson, lesson=self.get_lesson(), id=self.kwargs.get('specific_lesson_pk'))
  
  def get_student(self):
    return get_object_or_404(Student, id=self.kwargs.get('student_pk'))
  
  def get_object(self):
    try:
      homework = Homework.objects.get(student=self.get_student(), specific_lesson=self.get_specific_lesson())
    except Homework.DoesNotExist:
      homework = None
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
      'specific_lesson': SpecificLessonSerializer(specific_lesson).data,
      'note': NoteNameSerializer(specific_lesson.notes.filter(student=student).first()).data
    }
    return Response(data, status=status.HTTP_200_OK)
  
  def put(self, request: Request, *args, **kwargs):
    instance = self.get_object()
    if instance:
      return self.update(request, *args, **kwargs)
    request.data.pop('id')
    return self.create(request, *args, **kwargs)
  
  @extend_schema(exclude=True)
  def patch(self, request, *args, **kwargs):
    pass