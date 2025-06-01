from rest_framework import generics

from api.models import Subject
from api.serializers import SubjectSerializer

class SubjectListView(generics.ListAPIView):
  queryset = Subject.objects.all()
  serializer_class = SubjectSerializer
  
  def get_queryset(self):
    user = self.request.user.user
    if user.is_teacher:
      teacher = user.teacher
      return self.queryset.filter(name__in=teacher.subject_names.all()) 
    else:
      student = user.student
      if student.subscription:
        return self.queryset.filter(name__in=student.klass.school.subjects.all())
      return self.queryset.filter(name__in=student.klass.lessons.all(), grade=student.klass.grade)