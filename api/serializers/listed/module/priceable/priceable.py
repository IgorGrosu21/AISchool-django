from rest_framework.serializers import ModelSerializer

class PriceableSerializer(ModelSerializer):
  class Meta:
    fields = '__all__'