from api.models import Parent

from .person import PersonNameSerializer

class ParentNameSerializer(PersonNameSerializer):
  class Meta:
    fields = ['id', 'user']
    model = Parent