from rest_framework.serializers import ModelSerializer, SerializerMethodField

class PriceableSerializer(ModelSerializer):
  currency = SerializerMethodField()
  
  def get_currency(self, obj):
    return obj.get_currency_display()
  
  class Meta:
    fields = ['currency', 'cost', 'name', 'slug']