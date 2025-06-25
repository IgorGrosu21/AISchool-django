from rest_framework.serializers import ModelSerializer, CharField, DateField, SerializerMethodField

from api.models import User, SpecificLesson

class SpecificLessonNameSerializer(ModelSerializer):
  id = CharField(required=False, allow_blank=True)
  date = DateField(format='%Y.%m.%d', input_formats=['%Y.%m.%d'])
  
  class Meta:
    fields = ['id', 'lesson', 'date', 'title', 'desc']
    model = SpecificLesson
    
class SpecificLessonNameForStudentSerializer(SpecificLessonNameSerializer):
  note = SerializerMethodField()
  
  def get_note(self, obj: SpecificLesson) -> str:
    user: User = self.context['request'].user.user
    notes_qs = obj.notes.filter(student=user.student)
    if notes_qs.exists():
      return notes_qs.first().value
  
  class Meta(SpecificLessonNameSerializer.Meta):
    fields = SpecificLessonNameSerializer.Meta.fields + ['note']
    
class SpecificLessonNameForTeacherSerializer(SpecificLessonNameSerializer):
  pass