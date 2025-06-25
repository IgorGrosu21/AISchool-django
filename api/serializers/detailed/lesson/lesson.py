from ..school import KlassWithStudentsSerializer
from ...listed import LessonSerializer

class DetailedLessonSerializer(LessonSerializer):
  klass = KlassWithStudentsSerializer(read_only=True)