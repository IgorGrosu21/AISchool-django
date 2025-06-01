from api.models import Task

from .priceable import PriceableSerializer

class TaskSerializer(PriceableSerializer):
  class Meta(PriceableSerializer.Meta):
    model = Task