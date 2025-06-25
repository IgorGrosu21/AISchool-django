from .priceable import DetailedPriceableView

from api.models import Task
    
class DetailedTaskView(DetailedPriceableView):
  queryset = Task.objects.all()
  priceables_name = 'tasks'
