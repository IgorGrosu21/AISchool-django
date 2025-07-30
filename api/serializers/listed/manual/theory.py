from rest_framework.serializers import ModelSerializer

from api.models import Theory

class TheorySerializer(ModelSerializer):
  class Meta:
    fields = ['name', 'slug']
    model = Theory