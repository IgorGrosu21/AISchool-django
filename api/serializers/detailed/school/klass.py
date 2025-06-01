from api.models import Student, Lesson

from ..can_edit import CanEditSerializer
from ...listed import StudentSerializer, LessonSerializer, KlassSerializer
    
class DetailedKlassSerializer(KlassSerializer, CanEditSerializer):
  students = StudentSerializer(many=True)
  lessons = LessonSerializer(many=True)
  
  class Meta(KlassSerializer.Meta):
    fields = '__all__'
  
  def get_students(self, validated_data):
    students_data = validated_data.pop('students')
    students = Student.objects.none()
    for student_data in students_data:
      id = student_data.pop('id')
      students_qs = Student.objects.filter(id=id)
      students_qs.update(is_manager=student_data.pop('is_manager'))
      students |= students_qs
    return students, validated_data
  
  def get_lessons(self, validated_data):
    lessons_data = validated_data.pop('lessons')
    lessons = Lesson.objects.none()
    return lessons, validated_data
  
  def update(self, klass, validated_data):
    _, validated_data = self.get_students(validated_data)
    _, validated_data = self.get_lessons(validated_data)
    
    return super().update(klass, validated_data)