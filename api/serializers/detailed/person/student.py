from api.models import Student, Klass, Balance

from ...listed import KlassSerializer, StudentSerializer
from .person import DetailedPersonSerializer

class DetailedStudentSerializer(DetailedPersonSerializer, StudentSerializer):
  klass = KlassSerializer()
  
  class Meta(StudentSerializer.Meta):
    fields = StudentSerializer.Meta.fields + ['klass']
    nested_fields = {
      'one': {
        **StudentSerializer.Meta.nested_fields.get('one', {}),
        'klass': 'retrieve'
      },
    }
  
  def update(self, instance: Student, validated_data: dict):
    klass_data = validated_data['klass']
    params = {
      'school_id': klass_data['school']['id'],
      'grade': klass_data['grade'],
      'letter': klass_data['letter']
    }
    klass_qs = Klass.objects.filter(**params)
    if klass_qs.exists():
      validated_data['klass'] = {'id': klass_qs.first().id}
    else:
      params['profile'] = 'R' if params['letter'] == 'A' else 'U'
      validated_data['klass'] = {'id': Klass.objects.create(**params).id}
    instance = super().update(instance, validated_data)
    if not instance.balance:
      instance.balance = Balance.objects.create()
      instance.save()
    return instance