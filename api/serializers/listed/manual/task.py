from rest_framework.serializers import ModelSerializer, SerializerMethodField

from api.models import Task

class TaskSerializer(ModelSerializer):
  currency = SerializerMethodField()

  def get_currency(self, obj) -> str:
    return obj.get_currency_display()

  class Meta:
    model = Task
    fields = ['currency', 'cost', 'name', 'slug']