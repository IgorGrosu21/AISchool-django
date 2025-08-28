from rest_framework import generics
from drf_spectacular.utils import extend_schema
from django.shortcuts import get_object_or_404

from api.models import Subject, Student, Teacher, School, Klass
from api.serializers import SubjectNameSerializer

@extend_schema(tags=['api / subject'])
class SubjectNamesView(generics.ListAPIView):
  queryset = Subject.objects.all()
  serializer_class = SubjectNameSerializer
  
@extend_schema(tags=['api / subject'])
class TeachedSubjectsView(generics.ListAPIView):
  queryset = Subject.objects.all()
  serializer_class = SubjectNameSerializer
  
  def get_queryset(self):
    teacher_pk, school_slug, klass_slug = self.kwargs.get('teacher_pk'), self.kwargs.get('school_slug'), self.kwargs.get('klass_slug')
    teacher = get_object_or_404(Teacher, pk=teacher_pk)
    school = get_object_or_404(School, slug=school_slug)
    klass = get_object_or_404(Klass, school=school, slug=klass_slug)
    
    subject_ids = klass.lessons.filter(teacher=teacher).values_list('subject_id', flat=True)
    
    return teacher.subjects.filter(id__in=subject_ids)

@extend_schema(tags=['api / subject'])
class StudiedSubjectsView(generics.ListAPIView):
  queryset = Subject.objects.all()
  serializer_class = SubjectNameSerializer
  
  def get_queryset(self):
    student_pk = self.kwargs.get('student_pk')
    student = get_object_or_404(Student, pk=student_pk)
    return student.klass.subjects.distinct()