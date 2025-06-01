from api.models import Teacher

from .person import PersonSerializer

class TeacherSerializer(PersonSerializer):
  class Meta:
    fields = ['id', 'user']
    model = Teacher