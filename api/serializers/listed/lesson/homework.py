from rest_framework.serializers import ModelSerializer

from api.models import Homework

from ...media import MediaSerializer

class HomeworkSerializer(ModelSerializer):
  media = MediaSerializer(many=True)
  
  class Meta:
    exclude = ['id', 'specific_lesson', 'student']
    model = Homework