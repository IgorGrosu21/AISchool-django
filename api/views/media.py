from rest_framework import generics, status
from rest_framework.views import Response, Request
from rest_framework.parsers import MultiPartParser
from drf_spectacular.utils import extend_schema
from django.shortcuts import get_object_or_404

from utils.parsers import CamelCaseJSONParser
from api.models import WithFiles
from api.serializers import MediaSerializer, DetailedMediaSerializer

ALLOWED_IMAGE_TYPES = {'image/jpeg', 'image/png', 'image/gif', 'image/webp'}
ALLOWED_FILE_TYPES = ALLOWED_IMAGE_TYPES | {'application/pdf', 'text/plain', 'application/msword', 
                      'application/vnd.openxmlformats-officedocument.wordprocessingml.document'}
MAX_FILE_SIZE = 10 * 1024 * 1024  # 10MB

def validate_file_type(file, allowed_types):
    """Validate file type"""
    if file.content_type not in allowed_types:
        raise ValueError(f'File type {file.content_type} not allowed')
    return True

def validate_file_size(file, max_size):
    """Validate file size"""
    if file.size > max_size:
        raise ValueError(f'File size {file.size} exceeds maximum {max_size}')
    return True

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
  def patch(self, request: Request, *args, **kwargs):
    instance = self.get_object()
    media = getattr(instance, self.media_field)
    serializer = MediaSerializer(media, data=request.data)
    serializer.is_valid(raise_exception=True)
    file = serializer.validated_data.get('file')
    setattr(instance, self.media_field, file)
    instance.save()
    file = getattr(instance, self.media_field)
    return Response(file.get_absolute_url(), status=status.HTTP_200_OK)
  
  def perform_destroy(self, instance):
    if not hasattr(self, 'check_object_permissions'):
      self.check_object_permissions(self.request, instance)
    
    media = getattr(instance, self.media_field)
    media.delete()
  
class DetailedMediaView(generics.CreateAPIView, generics.DestroyAPIView):
  parser_classes = [MultiPartParser]
  serializer_class = DetailedMediaSerializer
  container_field: str
  
  def get_container(self) -> WithFiles: pass
  
  def get_object(self):
    pk = self.request.query_params.get('id', None)
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
    
    try:
      validate_file_type(file, ALLOWED_FILE_TYPES)
    except ValueError as e:
      raise ValueError(f"File type not allowed: {file.content_type}")
    
    try:
      validate_file_size(file, MAX_FILE_SIZE)
    except ValueError as e:
      raise ValueError(f"File too large: {file.size} bytes (max: {MAX_FILE_SIZE})")
    
    photo = container.files.create(file=file, **{self.container_field: container})
    serializer = self.serializer_class(photo)
    return Response(serializer.data, status=status.HTTP_201_CREATED)