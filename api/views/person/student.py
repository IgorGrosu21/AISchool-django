from api.models import Student
from api.permissions import IsSelfOrReadonly, IsStudentOrReadonly
from api.serializers import DetailedStudentSerializer

from .person import DetailedPersonView

class DetailedStudentView(DetailedPersonView):
  queryset = Student.objects.all()
  serializer_class = DetailedStudentSerializer
  permission_classes = [IsStudentOrReadonly, IsSelfOrReadonly]