from rest_framework.serializers import ModelSerializer, UUIDField

from api.models import SubjectType, Media

class SubjectTypeSerializer(ModelSerializer):
  id = UUIDField()
  
  class Meta:
    fields = ['id', 'name']
    model = SubjectType
    
  def to_representation(self, instance):
    r = super().to_representation(instance)
    r['image'] = Media.append_prefix(f'subjects/{instance.name}.png')
    return r