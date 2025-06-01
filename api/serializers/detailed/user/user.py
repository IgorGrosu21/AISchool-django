from api.models import Social, City

from ..can_edit import CanEditSerializer
from ...listed import SocialSerializer, CitySerializer, UserSerializer

class DetailedUserSerializer(UserSerializer, CanEditSerializer):
  socials = SocialSerializer(many=True, required=False, allow_null=True)
  city = CitySerializer()
  
  class Meta(UserSerializer.Meta):
    fields = UserSerializer.Meta.fields + ['socials', 'city', 'lang', 'can_edit']
  
  def get_socials(self, user, validated_data):
    socials_data = validated_data.pop('socials')
    socials = []
    if len(socials_data) == len(user.socials.all()):
      existing = set()
      to_add = set()
      for social_data in socials_data:
        type, link = social_data.pop('type'), social_data.pop('link')
        qs = user.socials.exclude(id__in=existing).filter(type=type, link=link)
        if qs.exists():
          existing.add(qs.first().id)
        else:
          to_add.add({type: type, link: link})
      user.socials.exclude(id__in=existing).delete()
      for new in to_add:
        socials.append(Social.objects.create(user=user, type=new['type'], link=new['link']))
    else:
      user.socials.all().delete()
      for social_data in socials_data:
        socials.append(Social.objects.create(user=user, type=social_data.pop('type'), link=social_data.pop('link')))
    return socials
  
  def get_city(self, validated_data):
    city_data = validated_data.pop('city')
    city = City.objects.get(id=city_data.get('id'))
    return city, validated_data
  
  def update(self, user, validated_data):
    socials, validated_data = self.get_socials(user, validated_data)
    user.socials.set(socials)
    city, validated_data = self.get_city(validated_data)
    user.city = city
    user.save()
    return super().update(user, validated_data)