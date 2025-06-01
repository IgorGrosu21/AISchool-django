from rest_framework.serializers import SerializerMethodField, Serializer

class CanEditSerializer(Serializer):
  can_edit = SerializerMethodField()
  
  def get_can_edit(self, obj):
    user = self.context['request'].user.user
    return user.id in obj.allowed_to_edit