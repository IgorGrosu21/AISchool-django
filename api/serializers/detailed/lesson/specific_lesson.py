from rest_framework.serializers import SerializerMethodField

from api.models import User, SpecificLesson

from .lesson import DetailedLessonSerializer
from ..can_edit import CanEditSerializer
from ...listed import LessonSerializer, NoteSerializer, HomeworkSerializer, StudentSerializer
from ...name import SpecificLessonNameSerializer, SpecificLessonNameForStudentSerializer, SpecificLessonNameForTeacherSerializer
from ...media import DetailedMediaSerializer

from ..._helpers import EditableSerializer

class DetailedSpecificLessonSerializer(EditableSerializer, SpecificLessonNameSerializer, CanEditSerializer):
  files = DetailedMediaSerializer(many=True, read_only=True)
  
  class Meta(SpecificLessonNameSerializer.Meta):
    fields = SpecificLessonNameSerializer.Meta.fields + ['can_edit', 'files', 'links']
    nested_fields = {
      'one': {
        'lesson': 'retrieve'
      }
    }
    
class DetailedSpecificLessonForStudentSerializer(DetailedSpecificLessonSerializer, SpecificLessonNameForStudentSerializer):
  lesson = LessonSerializer()
  note = SerializerMethodField()
  homework = SerializerMethodField()
  student = SerializerMethodField()
  
  def get_note(self, obj: SpecificLesson) -> str:
    user: User = self.context['request'].user.user
    notes_qs = obj.notes.filter(student=user.student)
    if notes_qs.exists():
      return NoteSerializer(notes_qs.first(), context=self.context).data
    
  def get_homework(self, obj: SpecificLesson):
    user: User = self.context['request'].user.user
    homeworks_qs = obj.homeworks.filter(student=user.student)
    if homeworks_qs.exists():
      return HomeworkSerializer(homeworks_qs.first(), context=self.context).data
    
  def get_student(self, obj: SpecificLesson):
    user: User = self.context['request'].user.user
    return StudentSerializer(user.student).data
  
  class Meta(DetailedSpecificLessonSerializer.Meta):
    fields = DetailedSpecificLessonSerializer.Meta.fields + ['note', 'homework', 'student']
    
class DetailedSpecificLessonForTeacherSerializer(DetailedSpecificLessonSerializer, SpecificLessonNameForTeacherSerializer):
  lesson = DetailedLessonSerializer()
  notes = NoteSerializer(many=True)
  homeworks = HomeworkSerializer(many=True)
  
  class Meta(DetailedSpecificLessonSerializer.Meta):
    fields = DetailedSpecificLessonSerializer.Meta.fields + ['notes', 'homeworks']
    nested_fields = {
      'one': DetailedSpecificLessonSerializer.Meta.nested_fields.get('one', {}),
      'many': {
        'notes': 'mutate',
        'homeworks': 'mutate'
      }
    }