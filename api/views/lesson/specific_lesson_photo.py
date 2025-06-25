from datetime import datetime
from rest_framework import generics, status
from rest_framework.views import Response

from api.models import SpecificLesson, Lesson, Klass, SpecificLessonPhoto
from api.serializers import DetailedMediaSerializer
    
class SpecificLessonPhotosView(generics.UpdateAPIView, generics.DestroyAPIView):
  queryset = SpecificLesson.objects.all()
  serializer_class = DetailedMediaSerializer
  
  def get_lesson(self):
    klass = Klass.objects.get(school=self.kwargs.get('school'), id=self.kwargs.get('klass'))
    return Lesson.objects.get(klass=klass, id=self.kwargs.get('lesson'))
  
  def get_date(self):
    return datetime.strptime(self.kwargs.get('date'), '%Y.%m.%d').date()
  
  def get_object(self):
    specific_lessons_qs = self.queryset.filter(lesson=self.get_lesson(), date=self.get_date())
    if specific_lessons_qs.exists():
      return specific_lessons_qs.first()
    return None
  
  def put(self, request, *args, **kwargs):
    specific_lesson = self.get_object()
    serializer = self.serializer_class(data=request.data)
    if serializer.is_valid():
      file = serializer.validated_data.get('file')
      specific_lesson_photo = SpecificLessonPhoto.objects.create(file=file, specific_lesson=specific_lesson)
      serializer = self.serializer_class(specific_lesson_photo)
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  
  def delete(self, request, *args, **kwargs):
    pk = self.kwargs.get('pk', None)
    if pk:
      specific_lesson = self.get_object()
      try:
        specific_lesson_photo = specific_lesson.files.get(pk=pk)
        specific_lesson_photo.delete()
      except:
        pass
    return Response(None, status=status.HTTP_204_NO_CONTENT)
    