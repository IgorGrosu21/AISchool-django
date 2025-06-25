from api.models import Student

from .person import PersonNameSerializer

class StudentNameSerializer(PersonNameSerializer):
  class Meta:
    fields = ['id', 'user']
    model = Student