from rest_framework import generics, status
from rest_framework.views import Response, Request
from rest_framework.parsers import MultiPartParser
from drf_spectacular.utils import extend_schema
from django.shortcuts import get_object_or_404

from utils.parsers import CamelCaseJSONParser
from api.models import WithFiles
from api.serializers import MediaSerializer, DetailedMediaSerializer

class MediaView(generics.GenericAPIView):
  parser_classes = [CamelCaseJSONParser, MultiPartParser]
  media_field: str
  
  @extend_schema(
    request={
      'multipart/form-data': {
        'type': 'object',
        'properties': { 'file': { 'type': 'string', 'format': 'binary' } },
        'required': ['file']
      }
    },
    responses=MediaSerializer
  )
  def patch(self, request, *args, **kwargs):
    instance = self.get_object()
    media = getattr(instance, self.media_field)
    serializer = MediaSerializer(media, data=request.data)
    serializer.is_valid(raise_exception=True)
    file = serializer.validated_data.get('file')
    setattr(instance, self.media_field, file)
    instance.save()
    return Response(serializer.data, status=status.HTTP_200_OK)
  
  def perform_destroy(self, instance):
    media = getattr(instance, self.media_field)
    media.delete()
  
class DetailedMediaView(generics.CreateAPIView, generics.DestroyAPIView):
  parser_classes = [MultiPartParser]
  serializer_class = DetailedMediaSerializer
  container_field: str
  
  def get_container(self) -> WithFiles: pass
  
  def get_object(self):
    pk = self.request.query_params.get('pk', None)
    container = self.get_container()
    return get_object_or_404(container.files, pk=pk)
  
  @extend_schema(
    request={
      'multipart/form-data': {
        'type': 'object',
        'properties': { 'file': { 'type': 'string', 'format': 'binary' } },
        'required': ['file']
      }
    }
  )
  def post(self, request: Request, *args, **kwargs):
    container = self.get_container()
    serializer = self.serializer_class(data=request.data)
    serializer.is_valid(raise_exception=True)
    file = serializer.validated_data.get('file')
    photo = container.files.create(file=file, **{self.container_field: container})
    serializer = self.serializer_class(photo)
    return Response(serializer.data, status=status.HTTP_201_CREATED)