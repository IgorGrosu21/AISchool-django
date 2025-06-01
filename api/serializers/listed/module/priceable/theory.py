from api.models import Theory

from .priceable import PriceableSerializer

class TheorySerializer(PriceableSerializer):
  class Meta(PriceableSerializer.Meta):
    model = Theory