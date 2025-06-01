from rest_framework.serializers import ModelSerializer

from api.models import Topic

class TopicSerializer(ModelSerializer):
  class Meta:
    fields = '__all__'
    model = Topic