from rest_framework.serializers import Serializer, UUIDField, ImageField

class MediaSerializer(Serializer):
  file = ImageField()
    
  def to_representation(self, instance):
    return instance.get_absolute_url()

class DetailedMediaSerializer(Serializer):
  id = UUIDField()
  file = ImageField()
  
  def to_representation(self, instance):
    r = super().to_representation(instance)
    r['file'] = instance.get_absolute_url()
    return r