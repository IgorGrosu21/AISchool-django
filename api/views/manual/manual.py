from rest_framework import generics
from drf_spectacular.utils import extend_schema

from api.models import User, Manual
from api.serializers import ManualSerializer, DetailedManualSerializer

@extend_schema(tags=['api / manual'])
class ManualListView(generics.ListAPIView):
  queryset = Manual.objects.all()
  serializer_class = ManualSerializer
  
  def get_queryset(self):
    user: User = self.request.user.user
    if user.account.is_staff:
      return self.queryset.filter(subject__type__country=user.city.region.country)
    if user.is_teacher:
      teacher = user.teacher
      return self.queryset.filter(subject__in=teacher.subjects.all()) 
    else:
      student = user.student
      if student.subscription:
        return self.queryset.filter(subject__type__country=user.city.region.country)
      return self.queryset.filter(subject__in=student.klass.subjects.all(), grade=student.klass.grade)
    
@extend_schema(tags=['api / manual'])
class DetailedManualView(generics.RetrieveAPIView):
  queryset = Manual.objects.all()
  serializer_class = DetailedManualSerializer
  lookup_field = 'slug'