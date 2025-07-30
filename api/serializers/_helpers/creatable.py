from rest_framework.serializers import ModelSerializer, CharField

class CreatableSerializer(ModelSerializer):
  id = CharField(allow_blank=True, required=False)