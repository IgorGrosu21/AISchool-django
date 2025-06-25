from datetime import datetime
from rest_framework import generics, status
from rest_framework.views import Response

from api.models import User, SpecificLesson, Lesson, Klass
from api.serializers import SpecificLessonNameForStudentSerializer, SpecificLessonNameForTeacherSerializer
from api.serializers import DetailedSpecificLessonForStudentSerializer, DetailedSpecificLessonForTeacherSerializer
from api.serializers import LessonSerializer, DetailedLessonSerializer

class SpecificLessonNamesView(generics.ListAPIView):
  queryset = SpecificLesson.objects.all()
  
  def get_serializer_class(self):
    user: User = self.request.user.user
    if user.is_student:
      return SpecificLessonNameForStudentSerializer
    else:
      return SpecificLessonNameForTeacherSerializer
  
  def get_queryset(self):
    start_str, end_str = self.kwargs.get('date_range').split('-')
    try:
      klass = Klass.objects.get(school=self.kwargs.get('school'), id=self.kwargs.get('klass'))
      start_date = datetime.strptime(start_str, '%Y.%m.%d').date()
      end_date = datetime.strptime(end_str, '%Y.%m.%d').date()
      return self.queryset.filter(lesson__klass=klass, date__gte=start_date, date__lte=end_date)
    except:
      return self.queryset.none()
    
class DetailedSpecificLessonView(generics.RetrieveUpdateDestroyAPIView):
  queryset = SpecificLesson.objects.all()
  
  def get_serializer_class(self):
    user: User = self.request.user.user
    if user.is_student:
      return DetailedSpecificLessonForStudentSerializer
    else:
      return DetailedSpecificLessonForTeacherSerializer
  
  def get_lesson(self):
    klass = Klass.objects.get(school=self.kwargs.get('school'), id=self.kwargs.get('klass'))
    return Lesson.objects.get(klass=klass, id=self.kwargs.get('lesson'))
  
  def get_date(self):
    return datetime.strptime(self.kwargs.get('date'), '%Y.%m.%d').date()
  
  def get_object(self):
    specific_lessons_qs = SpecificLesson.objects.filter(lesson=self.get_lesson(), date=self.get_date())
    if specific_lessons_qs.exists():
      return specific_lessons_qs.first()
    return None
  
  def get(self, request, *args, **kwargs):
    instance = self.get_object()
    if instance:
      return super().get(request, *args, **kwargs)
    user: User = request.user.user
    data = { 'id': '', 'date': self.kwargs.get('date'), 'desc': '', 'title': '', 'photos': [] }
    lesson = self.get_lesson()
    if user.is_student:
      lesson_serializer_class = LessonSerializer
      data = { **data, 'note': None, 'homework': None }
    else:
      lesson_serializer_class = DetailedLessonSerializer
      data = { **data, 'notes': [], 'homeworks': [] }
    return Response({ **data, 'lesson': lesson_serializer_class(lesson).data, 'can_edit': user.is_teacher }, status=status.HTTP_200_OK)
  
  def put(self, request, *args, **kwargs):
    instance = self.get_object()
    if instance:
      return super().put(request, *args, **kwargs)
    instance = SpecificLesson.objects.create(lesson=self.get_lesson(), date=self.get_date())
    data = {key: value for key, value in request.data.items() if key != 'id'}
    for raw_note in data.get('notes', []):
      raw_note['specific_lesson'] = str(instance.id)
    serializer = self.get_serializer_class()(instance, data=data, context={'request': request})
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
      instance.delete()
    return Response(None, status=status.HTTP_400_BAD_REQUEST)
    