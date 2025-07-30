from rest_framework import generics
from drf_spectacular.utils import extend_schema

from api.permisions import IsSchoolManagerOrReadonly, CanEditSchool
from api.models import School
from api.serializers import SchoolNameSerializer, SchoolSerializer
from api.serializers import DetailedSchoolSerializer, SchoolWithKlassesSerializer, SchoolWithTimetableSerializer

from ..media import MediaView

@extend_schema(tags=['api / school'])
class SchoolNamesView(generics.ListAPIView):
  queryset = School.objects.only('id', 'name')
  serializer_class = SchoolNameSerializer
  
  def get_queryset(self):
    return self.queryset.filter(city=self.request.user.user.city)

@extend_schema(tags=['api / school'])
class SchoolListView(SchoolNamesView):
  queryset = School.objects.all()
  serializer_class = SchoolSerializer

@extend_schema(tags=['api / school'])
class DetailedSchoolView(generics.RetrieveUpdateAPIView, MediaView):
  queryset = School.objects.all()
  serializer_class = DetailedSchoolSerializer
  permission_classes = [IsSchoolManagerOrReadonly, CanEditSchool]
  media_field = 'preview'

@extend_schema(tags=['api / school'])
class SchoolKlassesView(generics.RetrieveUpdateAPIView):
  queryset = School.objects.all()
  serializer_class = SchoolWithKlassesSerializer
  permission_classes = [IsSchoolManagerOrReadonly, CanEditSchool]
  
  @extend_schema(exclude=True)
  def patch(self, request, *args, **kwargs):
    pass

@extend_schema(tags=['api / school'])
class SchoolTimetableView(generics.RetrieveUpdateAPIView):
  queryset = School.objects.all()
  serializer_class = SchoolWithTimetableSerializer
  permission_classes = [IsSchoolManagerOrReadonly, CanEditSchool]
  
  @extend_schema(exclude=True)
  def patch(self, request, *args, **kwargs):
    pass