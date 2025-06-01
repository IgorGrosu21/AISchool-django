from api.models import Klass, Balance

from ...listed import KlassSerializer, ModuleProgressSerializer, StudentSerializer
from .person import DetailedPersonSerializer

class DetailedStudentSerializer(DetailedPersonSerializer, StudentSerializer):
  klass = KlassSerializer()
  modules_progress = ModuleProgressSerializer(many=True)
  
  class Meta(StudentSerializer.Meta):
    fields = '__all__'
  
  def get_klass(self, validated_data):
    klass_data = validated_data.pop('klass')
    school_id, grade, letter = klass_data.get('school').get('id'), klass_data.get('grade'), klass_data.get('letter')
    klass, _ = Klass.objects.get_or_create(school=school_id, grade=grade, letter=letter)
    return klass, validated_data
  
  def update(self, student, validated_data):
    if not student.balance:
      student.balance = Balance.objects.create()
    klass, validated_data = self.get_klass(validated_data)
    student.klass = klass
    student.save()
    return super().update(student, validated_data)