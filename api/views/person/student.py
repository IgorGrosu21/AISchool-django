from rest_framework import generics

from api.models import Student
from api.serializers import DetailedStudentSerializer

class DetailedStudentView(generics.RetrieveUpdateAPIView):
  queryset = Student.objects.all()
  serializer_class = DetailedStudentSerializer