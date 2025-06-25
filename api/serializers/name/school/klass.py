from rest_framework.serializers import CharField

from api.models import Klass

from ..._helpers import EditableSerializer

class KlassNameSerializer(EditableSerializer):
  id = CharField(allow_blank=True, required=False)
  
  class Meta:
    fields = ['id', 'grade', 'letter', 'profile', 'school']
    model = Klass