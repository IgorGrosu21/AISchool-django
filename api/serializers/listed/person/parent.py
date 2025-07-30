from .person import PersonSerializer
from ...name import ParentNameSerializer

class ParentSerializer(PersonSerializer, ParentNameSerializer):
  class Meta(PersonSerializer.Meta, ParentNameSerializer.Meta):
    pass