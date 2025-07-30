from rest_framework.serializers import DateField, SerializerMethodField

from api.models import SpecificLesson, Student

from ..._helpers import CreatableSerializer

class SpecificLessonNameSerializer(CreatableSerializer):
  date = DateField(format='%Y.%m.%d', input_formats=['%Y.%m.%d'])
  
  class Meta:
    fields = ['id', 'lesson', 'date', 'title', 'desc']
    model = SpecificLesson
    
class SpecificLessonWithHomeworkSerializer(SpecificLessonNameSerializer):
  note = SerializerMethodField()
  homework = SerializerMethodField()
  
  def __init__(self, *args, **kwargs):
    context = kwargs.get('context')
    self.student: Student = context['request'].user.user.student
  
  def get_note(self, obj: SpecificLesson) -> str | None:
    note_qs = obj.notes.filter(student=self.student)
    if note_qs.exists():
      return note_qs.first().value
    return None
  
  def get_homework(self, obj: SpecificLesson) -> str | None:
    homework_qs = obj.homeworks.filter(student=self.student)
    if homework_qs.exists():
      return homework_qs.first().id
    return None
  
  class Meta:
    fields = SpecificLessonNameSerializer.Meta.fields + ['note', 'homework']