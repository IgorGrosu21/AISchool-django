from datetime import datetime
from rest_framework import generics, mixins
from rest_framework.views import Request
from drf_spectacular.utils import extend_schema
from django.shortcuts import get_object_or_404

from api.permissions import IsTeacher, CanEditNote
from api.models import Note, Student, Teacher, Lesson, Klass, Subject, School, SpecificLesson
from api.serializers import NoteSerializer

@extend_schema(tags=['api / lesson'])
class StudentNoteListView(generics.ListAPIView):
  queryset = Note.objects.all()
  serializer_class = NoteSerializer
  
  def get_queryset(self):
    student = get_object_or_404(Student, pk=self.kwargs.get('student_pk'))
    start_str, end_str = self.kwargs.get('date_range').split('-')
    start_date = datetime.strptime(start_str, '%Y.%m.%d').date()
    end_date = datetime.strptime(end_str, '%Y.%m.%d').date()
    return self.queryset.filter(
      student=student,
      specific_lesson__date__gte=start_date,
      specific_lesson__date__lte=end_date
    )

@extend_schema(tags=['api / lesson'])
class TeacherNoteListView(generics.ListAPIView):
  queryset = Note.objects.all()
  serializer_class = NoteSerializer
  
  def get_queryset(self):
    teacher = get_object_or_404(Teacher, pk=self.kwargs.get('teacher_pk'))
    school = get_object_or_404(School, slug=self.kwargs.get('school_slug'))
    klass = get_object_or_404(Klass, school=school, slug=self.kwargs.get('klass_slug'))
    subject = get_object_or_404(Subject, slug=self.kwargs.get('subject_slug'))
    start_str, end_str = self.kwargs.get('date_range').split('-')
    start_date = datetime.strptime(start_str, '%Y.%m.%d').date()
    end_date = datetime.strptime(end_str, '%Y.%m.%d').date()
    return self.queryset.filter(
      specific_lesson__lesson__teacher=teacher,
      specific_lesson__lesson__klass=klass,
      specific_lesson__lesson__subject=subject,
      specific_lesson__date__gte=start_date,
      specific_lesson__date__lte=end_date
    )
    
class NoteCreateView(generics.CreateAPIView, mixins.UpdateModelMixin):
  queryset = Note.objects.all()
  serializer_class = NoteSerializer
  permission_classes = [IsTeacher, CanEditNote]
  
  def get_klass(self) -> Klass:
    return get_object_or_404(Klass, school__slug=self.kwargs.get('school_slug'), slug=self.kwargs.get('klass_slug'))

  def get_lesson(self) -> Lesson:
    klass = self.get_klass()
    return get_object_or_404(klass.lessons, id=self.kwargs.get('lesson_pk'))
  
  def get_student(self) -> Student:
    klass = self.get_klass()
    return get_object_or_404(klass.students, id=self.kwargs.get('student_pk'))
  
  def get_or_create_specific_lesson(self) -> tuple[SpecificLesson, bool]:
    lesson = self.get_lesson()
    specific_lesson_data = self.request.data.get('specific_lesson')
    specific_lesson_id = specific_lesson_data.get('id')
    if specific_lesson_id:
      return get_object_or_404(SpecificLesson, lesson=lesson, id=specific_lesson_id), False
    specific_lesson_date = datetime.strptime(specific_lesson_data.get('date'), '%Y.%m.%d').date()
    return SpecificLesson.objects.get_or_create(lesson=lesson, date=specific_lesson_date)
  
  def get_object(self):
    lesson = self.get_lesson()
    student = self.get_student()
    specific_lesson_data = self.request.data.get('specific_lesson')
    specific_lesson_id = specific_lesson_data.get('id')
    note_id = self.request.data.get('id')
    if specific_lesson_id and note_id:
      specific_lesson = get_object_or_404(SpecificLesson, lesson=lesson, id=specific_lesson_id)
      note = get_object_or_404(Note, id=note_id, specific_lesson=specific_lesson, student=student)
      self.check_object_permissions(self.request, note)
      return note
    return None
  
  def post(self, request: Request, *args, **kwargs):
    note = self.get_object()
    if note:
      return self.update(request, *args, **kwargs)
    specific_lesson, created = self.get_or_create_specific_lesson()
    request.data.pop('id')
    try:
      return self.create(request, *args, **kwargs)
    except Exception as e:
      if created:
        specific_lesson.delete()
      raise e
  
  def perform_create(self, serializer: NoteSerializer):
    specific_lesson, _ = self.get_or_create_specific_lesson()
    serializer.save(specific_lesson=specific_lesson, student=self.get_student())