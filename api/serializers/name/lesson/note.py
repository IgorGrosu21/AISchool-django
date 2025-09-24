from rest_framework.serializers import DateTimeField

from api.models import Note

from ..._helpers import CreatableSerializer

class NoteNameSerializer(CreatableSerializer):
  last_modified = DateTimeField('%d.%m, %H:%M', read_only=True)

  class Meta:
    fields = ['id', 'value', 'specific_lesson', 'student', 'comment', 'last_modified']
    model = Note