from rest_framework.serializers import ModelSerializer

from api.models import Note

from ..person import StudentSerializer

class NoteSerializer(ModelSerializer):
  student = StudentSerializer()
  
  class Meta:
    exclude = ['id', 'specific_lesson']
    model = Note