from rest_framework.serializers import ModelSerializer, CharField, DateTimeField

from api.models import Homework

from ...media import DetailedMediaSerializer

class HomeworkSerializer(ModelSerializer):
  id = CharField(required=False, allow_blank=True)
  files = DetailedMediaSerializer(many=True, read_only=True)
  last_modified = DateTimeField('%d.%m, %H:%M', read_only=True)
  
  class Meta:
    fields = ['id', 'specific_lesson', 'student', 'comment', 'links', 'files', 'last_modified']
    model = Homework