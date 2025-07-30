from api.models import Klass

from ..._helpers import CreatableSerializer

class KlassNameSerializer(CreatableSerializer):
  class Meta:
    fields = ['id', 'grade', 'letter', 'profile', 'school']
    model = Klass