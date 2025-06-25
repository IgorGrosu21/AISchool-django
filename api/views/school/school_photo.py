from rest_framework import generics, status
from rest_framework.views import Response

from api.models import School, SchoolPhoto
from api.serializers import DetailedMediaSerializer

class SchoolPhotoView(generics.UpdateAPIView, generics.DestroyAPIView):
  queryset = SchoolPhoto.objects.all()
  serializer_class = DetailedMediaSerializer
  
  def put(self, request, school_pk, pk = None, *args, **kwargs):
    if pk:
      return self.patch(request, school_pk, pk, *args, **kwargs)
    
    school = School.objects.get(pk=school_pk)
    serializer = self.serializer_class(data=request.data)
    if serializer.is_valid():
      file = serializer.validated_data.get('file')
      school_photo = SchoolPhoto.objects.create(file=file, school=school)
      serializer = self.serializer_class(school_photo)
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  
  def patch(self, request, school_pk, pk = None, *args, **kwargs):
    if not pk:
      return self.put(request, school_pk, pk, *args, **kwargs)
    
    school_photo = self.queryset.get(school__pk=school_pk, pk=pk)
    serializer = self.serializer_class(school_photo, data=request.data)
    if serializer.is_valid():
      file = serializer.validated_data.get('file')
      school_photo.file = file
      school_photo.save()
      serializer = self.serializer_class(school_photo)
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  
  def delete(self, request, school_pk, pk = None, *args, **kwargs):
    if pk:
      school_photo = self.queryset.get(school__pk=school_pk, pk=pk)
      school_photo.delete()
    return Response(None, status=status.HTTP_204_NO_CONTENT)