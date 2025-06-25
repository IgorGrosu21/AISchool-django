from api.models import Teacher

from .person import PersonNameSerializer

class TeacherNameSerializer(PersonNameSerializer):
  class Meta:
    fields = ['id', 'user']
    model = Teacher