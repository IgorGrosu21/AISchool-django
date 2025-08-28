from ...name import NoteNameSerializer, StudentNameSerializer
from .specific_lesson import SpecificLessonSerializer

class NoteSerializer(NoteNameSerializer):
  specific_lesson = SpecificLessonSerializer(read_only=True)
  student = StudentNameSerializer(read_only=True)