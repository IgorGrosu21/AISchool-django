from rest_framework.serializers import Serializer, FloatField

class ProgressSerializer(Serializer):
  subject = FloatField(allow_null=True)
  module = FloatField(allow_null=True)
  topic = FloatField(allow_null=True)