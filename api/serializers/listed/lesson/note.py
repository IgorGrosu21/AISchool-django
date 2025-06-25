from rest_framework.serializers import ModelSerializer, CharField, DateTimeField

from api.models import Note

class NoteSerializer(ModelSerializer):
  id = CharField(required=False, allow_blank=True)
  last_modified = DateTimeField('%d.%m, %H:%M', read_only=True)
  
  class Meta:
    fields = ['id', 'value', 'specific_lesson', 'student', 'comment', 'last_modified']
    model = Note