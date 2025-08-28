from rest_framework import generics
from drf_spectacular.utils import extend_schema
from django.shortcuts import get_object_or_404
from django.db.models import Q

from api.permissions import IsTeacherOrReadonly, CanEditKlass
from api.models import School, Klass, Teacher
from api.serializers import KlassSerializer, DetailedKlassSerializer

@extend_schema(tags=['api / school'])
class TeacherKlasses(generics.ListAPIView):
  queryset = Klass.objects.all()
  serializer_class = KlassSerializer
  
  def get_queryset(self):
    school_slug, teacher_pk = self.kwargs.get('school_slug'), self.kwargs.get('teacher_pk')
    school = get_object_or_404(School, slug=school_slug)
    teacher = get_object_or_404(Teacher, pk=teacher_pk)
    return self.queryset.filter(
      Q(lessons__teacher=teacher) | Q(teacher=teacher),
      school=school
    ).distinct()

@extend_schema(tags=['api / school'])
class DetailedKlassView(generics.RetrieveUpdateAPIView):
  queryset = Klass.objects.all()
  serializer_class = DetailedKlassSerializer
  permission_classes = [IsTeacherOrReadonly, CanEditKlass]
  
  def get_object(self):
    school_slug, slug = self.kwargs.get('school_slug'), self.kwargs.get('slug')
    school = get_object_or_404(School, slug=school_slug)
    klass = get_object_or_404(Klass, slug=slug, school=school)
    self.check_object_permissions(self.request, klass)
    return klass
  
  @extend_schema(exclude=True)
  def patch(self, request, *args, **kwargs):
    pass