from rest_framework import generics

from api.models import User, Subject
from api.serializers import SubjectSerializer, DetailedSubjectSerializer

class SubjectListView(generics.ListAPIView):
  queryset = Subject.objects.all()
  serializer_class = SubjectSerializer
  
  def get_queryset(self):
    user: User = self.request.user.user
    if user.account.is_staff:
      return self.queryset.filter(name__type__country=user.city.region.country)
    if user.is_teacher:
      teacher = user.teacher
      return self.queryset.filter(name__in=teacher.subject_names.all()) 
    else:
      student = user.student
      if student.subscription:
        return self.queryset.filter(name__type__country=user.city.region.country)
      return self.queryset.filter(name__in=student.klass.lessons.all(), grade=student.klass.grade)
    
class DetailedSubjectView(generics.RetrieveAPIView):
  queryset = Subject.objects.all()
  serializer_class = DetailedSubjectSerializer
  lookup_field = 'slug'