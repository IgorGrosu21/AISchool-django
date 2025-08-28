from rest_framework.serializers import ModelSerializer, UUIDField

class RetrieveableSerializer(ModelSerializer):
  id = UUIDField()