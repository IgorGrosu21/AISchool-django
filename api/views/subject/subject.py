from rest_framework import generics
from drf_spectacular.utils import extend_schema

from api.models import Subject
from api.serializers import SubjectNameSerializer

@extend_schema(tags=['api / subject'])
class SubjectNamesView(generics.ListAPIView):
  queryset = Subject.objects.all()
  serializer_class = SubjectNameSerializer