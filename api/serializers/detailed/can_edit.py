from rest_framework.serializers import SerializerMethodField, Serializer

from api.models import User

class CanEditSerializer(Serializer):
  can_edit = SerializerMethodField()
  
  def get_can_edit(self, obj) -> bool:
    user: User = self.context['request'].user.user
    if not user.account.is_verified:
      return False
    allowed_to_edit, verification_required = obj.allowed_to_edit
    if verification_required and not user.is_verified:
      return False
    return user.id in allowed_to_edit or user.account.is_staff