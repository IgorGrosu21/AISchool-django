from drf_spectacular.utils import extend_schema
from django.shortcuts import get_object_or_404

from api.permissions import IsSchoolManagerOrReadonly, CanEditSchool
from api.models import School

from ..media import DetailedMediaView

@extend_schema(tags=['api / school'])
class SchoolPhotoView(DetailedMediaView):
  permission_classes = [IsSchoolManagerOrReadonly, CanEditSchool]
  container_field = 'school'
  
  def get_container(self):
    school_slug = self.kwargs.get('school_slug')
    school = get_object_or_404(School, slug=school_slug)
    self.check_object_permissions(self.request, school)
    return school