from datetime import datetime
from rest_framework import generics, status
from rest_framework.views import Response

from api.models import User, Homework, HomeworkPhoto, SpecificLesson, Lesson, Klass
from api.serializers import DetailedMediaSerializer

class HomeworkPhotosView(generics.UpdateAPIView, generics.DestroyAPIView):
  queryset = Homework.objects.all()
  serializer_class = DetailedMediaSerializer
  
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
      homework_qs = self.queryset.filter(student=user.student, specific_lesson=self.get_specific_lesson())
      if homework_qs.exists():
        return homework_qs.first()
    return None
  
  def put(self, request, *args, **kwargs):
    homework = self.get_object()
    if homework == None:
      return Response(None, status=status.HTTP_403_FORBIDDEN)
    serializer = self.serializer_class(data=request.data)
    if serializer.is_valid():
      file = serializer.validated_data.get('file')
      specific_lesson_photo = HomeworkPhoto.objects.create(file=file, homework=homework)
      serializer = self.serializer_class(specific_lesson_photo)
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  
  def delete(self, request, *args, **kwargs):
    pk = self.kwargs.get('pk', None)
    if pk:
      user: User = self.request.user.user
      try:
        if user.is_student:
          homework = self.get_object()
          homework_photo = homework.files.get(pk=pk)
        else:
          specific_lesson = self.get_specific_lesson()
          homework_photo = HomeworkPhoto.objects.get(homework__specific_lesson=specific_lesson, pk=pk)
        homework_photo.delete()
      except:
        pass
    return Response(None, status=status.HTTP_204_NO_CONTENT)