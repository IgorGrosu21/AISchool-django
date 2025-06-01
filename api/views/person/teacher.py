from rest_framework import generics

from api.models import Teacher
from api.serializers import DetailedTeacherSerializer

class DetailedTeacherView(generics.RetrieveUpdateAPIView):
  queryset = Teacher.objects.all()
  serializer_class = DetailedTeacherSerializer
