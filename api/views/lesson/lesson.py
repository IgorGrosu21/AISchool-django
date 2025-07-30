from rest_framework import generics, exceptions
from drf_spectacular.utils import extend_schema
from django.shortcuts import get_object_or_404

from api.models import Lesson, Parent, Student, Teacher
from api.serializers import LessonNameSerializer

@extend_schema(tags=['api / lesson'])
class LessonNamesView(generics.ListAPIView):
  queryset = Lesson.objects.all()
  serializer_class = LessonNameSerializer
  
  def get_queryset(self):
    account_type = self.kwargs.get('account_type', None)
    pk = self.kwargs.get('person_pk')
    if account_type == 'parent':
      model = Parent
    elif account_type == 'student':
      model = Student
    elif account_type == 'teacher':
      model = Teacher
    else:
      raise exceptions.ParseError(code='invalid_account_type')
    person = get_object_or_404(model, pk=pk)
    return person.lessons.all()