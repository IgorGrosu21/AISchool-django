from rest_framework.serializers import Serializer, CharField, ImageField, FileField, ValidationError

from api.models import Media

ALLOWED_IMAGE_TYPES = {'image/jpeg', 'image/png', 'image/gif', 'image/webp'}
ALLOWED_FILE_TYPES = ALLOWED_IMAGE_TYPES | {'application/pdf', 'text/plain', 'application/msword',
                      'application/vnd.openxmlformats-officedocument.wordprocessingml.document'}
MAX_FILE_SIZE = 10 * 1024 * 1024  # 10MB

class MediaSerializer(Serializer):
  file = ImageField()

  def validate_file(self, value):
    if value.size > MAX_FILE_SIZE:
      raise ValidationError(f'File size must be no more than {MAX_FILE_SIZE / (1024*1024)}MB')

    if value.content_type not in ALLOWED_IMAGE_TYPES:
      raise ValidationError(f'File type {value.content_type} not allowed. Allowed types: {", ".join(ALLOWED_IMAGE_TYPES)}')

    return value

  def to_representation(self, instance: Media):
    return instance.get_absolute_url()

class DetailedMediaSerializer(Serializer):
  id = CharField(allow_blank=True, required=False)
  file = FileField()

  def validate_file(self, value):
    if value.content_type not in ALLOWED_FILE_TYPES:
      raise ValidationError(f'File type {value.content_type} not allowed. Allowed types: {", ".join(ALLOWED_FILE_TYPES)}')

    if value.size > MAX_FILE_SIZE:
      raise ValidationError(f'File size must be no more than {MAX_FILE_SIZE / (1024*1024)}MB')

    return value

  def to_representation(self, instance: Media):
    r = super().to_representation(instance)
    r['file'] = instance.get_absolute_url()
    return r