from api.permissions import IsParentOrReadonly, IsSelfOrReadonly
from api.models import Parent
from api.serializers import DetailedParentSerializer

from .person import DetailedPersonView

class DetailedParentView(DetailedPersonView):
  queryset = Parent.objects.all()
  serializer_class = DetailedParentSerializer
  permission_classes = [IsParentOrReadonly, IsSelfOrReadonly]