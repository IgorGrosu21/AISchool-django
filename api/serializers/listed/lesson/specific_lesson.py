from rest_framework.serializers import ModelSerializer

from api.models import SpecificLesson

from ...media import MediaSerializer
from .lesson import LessonSerializer
from .homework import HomeworkSerializer
from .note import NoteSerializer

class SpecificLessonSerializer(ModelSerializer):
  lesson = LessonSerializer()
  media = MediaSerializer(many=True)
  uploaded_homeworks = HomeworkSerializer(many=True, source='uploaded_homeworks')
  notes = NoteSerializer(many=True, source='given_notes')
  
  class Meta:
    exclude = ['id']
    model = SpecificLesson