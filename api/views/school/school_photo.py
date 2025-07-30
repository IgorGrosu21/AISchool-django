from drf_spectacular.utils import extend_schema
from django.shortcuts import get_object_or_404

from api.permisions import IsSchoolManagerOrReadonly, CanEditSchool
from api.models import School

from ..media import DetailedMediaView

@extend_schema(tags=['api / school'])
class SchoolPhotoView(DetailedMediaView):
  permission_classes = [IsSchoolManagerOrReadonly, CanEditSchool]
  container_field = 'school'
  
  def get_container(self):
    school_pk = self.kwargs.get('school_pk', None)
    school = get_object_or_404(School, pk=school_pk)
    self.check_object_permissions(self.request, school)
    return school