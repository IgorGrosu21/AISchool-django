from rest_framework import generics

from api.models import SubjectName
from api.serializers import SubjectNameSerializer

class SubjectNameListView(generics.ListAPIView):
  queryset = SubjectName.objects.all()
  serializer_class = SubjectNameSerializer