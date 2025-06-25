from rest_framework.serializers import ModelSerializer, UUIDField, SerializerMethodField

from api.models import SubjectName, Media

class SubjectNameSerializer(ModelSerializer):
  id = UUIDField()
  image = SerializerMethodField()
  
  def get_image(self, obj: SubjectName):
    return Media.append_prefix(f'subjects/{obj.type.name}.png')
  
  class Meta:
    fields = ['id', 'image', 'verbose_name']
    model = SubjectName