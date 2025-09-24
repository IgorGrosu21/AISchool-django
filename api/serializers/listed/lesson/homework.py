from rest_framework.serializers import DateTimeField

from api.models import Homework

from ..._helpers import CreatableSerializer
from ...media import DetailedMediaSerializer

class HomeworkSerializer(CreatableSerializer):
  files = DetailedMediaSerializer(many=True, read_only=True)
  last_modified = DateTimeField('%d.%m, %H:%M', read_only=True)

  class Meta:
    fields = ['id', 'student', 'comment', 'links', 'files', 'last_modified']
    model = Homework