from rest_framework.serializers import Serializer, UUIDField, ImageField, FileField

from api.models import Media

class MediaSerializer(Serializer):
  file = ImageField()
    
  def to_representation(self, instance: Media):
    return instance.get_absolute_url()

class DetailedMediaSerializer(Serializer):
  id = UUIDField(required=False)
  file = FileField()
  
  def to_representation(self, instance: Media):
    r = super().to_representation(instance)
    r['file'] = instance.get_absolute_url()
    return r