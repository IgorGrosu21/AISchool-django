from datetime import datetime
from rest_framework import generics, mixins, status, exceptions
from rest_framework.views import Response, Request
from drf_spectacular.utils import extend_schema
from django.shortcuts import get_object_or_404

from api.permissions import IsKlassManagerOrReadonly, IsTeacherOrReadonly, CanEditSpecificLesson
from api.models import School, SpecificLesson, Lesson, Klass, Student, Teacher
from api.serializers import SpecificLessonNameSerializer, SpecificLessonWithHomeworkSerializer
from api.serializers import LessonSerializer, StudentSerializer, DetailedSpecificLessonSerializer

@extend_schema(tags=['api / lesson'])
class SpecificLessonNamesView(generics.ListAPIView):
  queryset = SpecificLesson.objects.all()
  
  def get_serializer_class(self):
    if self.request.user.is_anonymous:
      return SpecificLessonNameSerializer
  
    account_type = self.get_account_type()
    if account_type == 'student':
      return SpecificLessonWithHomeworkSerializer
    return SpecificLessonNameSerializer
  
  def get_school(self) -> School:
    return get_object_or_404(School, slug=self.request.query_params.get('school'))
  
  def get_account_type(self) -> str:
    account_type = self.kwargs.get('account_type', '')
    allowed_types = ['teacher', 'student']
    if account_type in allowed_types:
      return account_type
    raise exceptions.ParseError(code='invalid_account_type')
  
  def get_person(self):
    account_type = self.get_account_type()
    pk = self.kwargs.get('person_pk')
    model = Teacher
    if account_type == 'student':
      model = Student
    return get_object_or_404(model, pk=pk)
  
  def get_queryset(self):
    start_str, end_str = self.kwargs.get('date_range').split('-')
    start_date = datetime.strptime(start_str, '%Y.%m.%d').date()
    end_date = datetime.strptime(end_str, '%Y.%m.%d').date()
    person = self.get_person()
    lessons_ids = person.lessons.values_list('id', flat=True)
    account_type = self.get_account_type()
    qs = self.queryset.filter(lesson__id__in=lessons_ids, date__gte=start_date, date__lte=end_date)
    if account_type == 'teacher':
      school = self.get_school()
      return qs.filter(lesson__klass__school=school)
    return qs

@extend_schema(tags=['api / lesson'])
class DetailedSpecificLessonView(generics.RetrieveUpdateDestroyAPIView, mixins.CreateModelMixin):
  permission_classes = [IsKlassManagerOrReadonly|IsTeacherOrReadonly, CanEditSpecificLesson]
  queryset = SpecificLesson.objects.all()
  serializer_class = DetailedSpecificLessonSerializer
  
  def get_lesson(self):
    klass: Klass = get_object_or_404(Klass, school__slug=self.kwargs.get('school_slug'), slug=self.kwargs.get('klass_slug'))
    return get_object_or_404(Lesson, klass__id=klass.id, id=self.kwargs.get('lesson_pk'))
  
  def get_date(self):
    return datetime.strptime(self.kwargs.get('date'), '%Y.%m.%d').date()
  
  def get_object(self):
    try:
      specific_lesson = SpecificLesson.objects.get(lesson=self.get_lesson(), date=self.get_date())
    except SpecificLesson.DoesNotExist:
      specific_lesson = None
    self.check_object_permissions(self.request, specific_lesson)
    return specific_lesson
  
  def get(self, request: Request, *args, **kwargs):
    instance = self.get_object()
    if instance:
      return self.retrieve(request, *args, **kwargs)
    lesson = self.get_lesson()
    data = {
      'id': '',
      'date': kwargs.get('date'),
      'lesson': LessonSerializer(lesson).data,
      'desc': '',
      'title': '',
      'files': [],
      'links': '',
      'students': StudentSerializer(lesson.students, many=True).data,
      'notes': [],
      'homeworks': [],
      'can_edit': True,
      'is_student': request.user.user.is_student
    }
    return Response(data, status=status.HTTP_200_OK)
  
  def put(self, request: Request, *args, **kwargs):
    instance = self.get_object()
    if instance:
      return self.update(request, *args, **kwargs)
    request.data.pop('id')
    raw_notes = request.data.pop('notes', [])
    response = self.create(request, *args, **kwargs)
    if len(raw_notes) > 0 and not request.user.user.is_student:
      for raw_note in raw_notes:
        raw_note['specific_lesson'] = str(instance.id)
      setattr(self.request, 'data', {'notes': raw_notes})
      return self.partial_update(self.request)
    return response
  
  @extend_schema(exclude=True)
  def patch(self, request, *args, **kwargs):
    pass
    