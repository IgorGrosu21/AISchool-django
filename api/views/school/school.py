from rest_framework import generics, status
from rest_framework.views import Response

from api.models import School, Media
from api.serializers import SchoolNameSerializer, SchoolSerializer, DetailedSchoolSerializer, MediaSerializer

class SchoolNamesView(generics.ListCreateAPIView):
  queryset = School.objects.only('id', 'name')
  serializer_class = SchoolNameSerializer
  
  def get_queryset(self):
    return self.queryset.filter(city=self.request.user.user.city)

class SchoolListView(SchoolNamesView):
  queryset = School.objects.all()
  serializer_class = SchoolSerializer

class DetailedSchoolView(generics.RetrieveUpdateDestroyAPIView):
  queryset = School.objects.all()
  serializer_class = DetailedSchoolSerializer
  
  def patch(self, request, pk, *args, **kwargs):
    school = School.objects.get(pk=pk)
    if not school.preview:
      serializer = MediaSerializer(data=request.data)
      if serializer.is_valid():
        preview = serializer.validated_data.get('file')
        school.preview = preview
        school.save()
        return Response(Media.append_prefix(school.preview.file.name), status=status.HTTP_201_CREATED)
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    serializer = MediaSerializer(school.preview, data=request.data)
    if serializer.is_valid():
      preview = serializer.validated_data.get('file')
      return Response(Media.append_prefix(school.preview.file.name), status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  
  def delete(self, request, pk, *args, **kwargs):
    school = School.objects.get(pk=pk)
    school.preview.delete()
    return Response(None, status=status.HTTP_204_NO_CONTENT)