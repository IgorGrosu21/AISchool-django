from rest_framework import generics
from drf_spectacular.utils import extend_schema
from django.shortcuts import get_object_or_404

from api.models import LessonTime, School
from api.serializers import LessonTimeNameSerializer

@extend_schema(tags=['api / lesson'])
class LessonTimeNamesView(generics.ListAPIView):
  queryset = LessonTime.objects.all()
  serializer_class = LessonTimeNameSerializer
  
  def get_queryset(self):
    school = get_object_or_404(School, pk=self.kwargs.get('school_pk'))
    return self.queryset.filter(school=school)