from datetime import datetime
from rest_framework import generics, status
from rest_framework.views import Response

from api.models import User, Homework, SpecificLesson, Lesson, Klass
from api.serializers import HomeworkSerializer, DetailedMediaSerializer

class DetailedHomeworkView(generics.UpdateAPIView, generics.DestroyAPIView):
  queryset = Homework.objects.all()
  serializer_class = HomeworkSerializer
  photo_serializer_class = DetailedMediaSerializer
  
  def get_lesson(self):
    klass = Klass.objects.get(school=self.kwargs.get('school'), id=self.kwargs.get('klass'))
    return Lesson.objects.get(klass=klass, id=self.kwargs.get('lesson'))
  
  def get_date(self):
    return datetime.strptime(self.kwargs.get('date'), '%Y.%m.%d').date()
  
  def get_specific_lesson(self):
    return SpecificLesson.objects.get(lesson=self.get_lesson(), date=self.get_date())
  
  def get_object(self):
    user: User = self.request.user.user
    if user.is_student:
      homework_qs = Homework.objects.filter(student=user.student, specific_lesson=self.get_specific_lesson())
      if homework_qs.exists():
        return homework_qs.first()
    return None
  
  def put(self, request, *args, **kwargs):
    if self.get_object():
      return super().put(request, *args, **kwargs)
    data = {key: value for key, value in request.data.items() if key != 'id'}
    serializer = self.serializer_class(data=data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)