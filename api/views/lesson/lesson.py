from rest_framework import generics, exceptions
from drf_spectacular.utils import extend_schema
from django.shortcuts import get_object_or_404

from api.models import School, Lesson, Parent, Student, Teacher
from api.serializers import LessonNameSerializer

@extend_schema(tags=['api / lesson'])
class LessonNamesView(generics.ListAPIView):
  queryset = Lesson.objects.all()
  serializer_class = LessonNameSerializer
  
  def get_queryset(self):
    account_type = self.kwargs.get('account_type')
    school = None
    pk = self.kwargs.get('person_pk')
    if account_type == 'parent':
      model = Parent
    elif account_type == 'student':
      model = Student
    elif account_type == 'teacher':
      model = Teacher
      school = get_object_or_404(School, slug=self.request.query_params.get('school'))
    else:
      raise exceptions.ParseError(code='invalid_account_type')
    person = get_object_or_404(model, pk=pk)
    if school:
      return person.lessons.filter(klass__school=school)
    return person.lessons.all()