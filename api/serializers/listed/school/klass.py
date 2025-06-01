from rest_framework.serializers import ModelSerializer, UUIDField

from api.models import Klass, Teacher, School

from ...name import SchoolNameSerializer
from ..person import TeacherSerializer

class KlassSerializer(ModelSerializer):
  id = UUIDField()
  teacher = TeacherSerializer(required=False, allow_null=True)
  school = SchoolNameSerializer()
  
  class Meta:
    fields = ['id', 'grade', 'letter', 'teacher', 'school', 'profile', 'networth']
    model = Klass
  
  def get_teacher(self, validated_data):
    teacher_data = validated_data.pop('teacher', None)
    if teacher_data:
      return Teacher.objects.get(id=teacher_data.get('id')), validated_data
    return None, validated_data
  
  def get_school(self, validated_data):
    school_data = validated_data.pop('school')
    school = School.objects.get(id=school_data.get('id'))
    return school, validated_data
  
  def update(self, klass, validated_data):
    teacher, validated_data = self.get_teacher(validated_data)
    if teacher:
      klass.teacher = teacher
      klass.save()
    _, validated_data = self.get_school(validated_data)
    return super().update(klass, validated_data)