from api.permisions import IsTeacherOrReadonly, IsSelfOrReadonly
from api.models import Teacher
from api.serializers import DetailedTeacherSerializer

from .person import DetailedPersonView

class DetailedTeacherView(DetailedPersonView):
  queryset = Teacher.objects.all()
  serializer_class = DetailedTeacherSerializer
  permission_classes = [IsTeacherOrReadonly, IsSelfOrReadonly]