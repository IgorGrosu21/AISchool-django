from .priceable import DetailedPriceableView

from api.models import Theory
    
class DetailedTheoryView(DetailedPriceableView):
  queryset = Theory.objects.all()
  priceables_name = 'theories'
