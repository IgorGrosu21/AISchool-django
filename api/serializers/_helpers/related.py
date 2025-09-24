from functools import wraps

from rest_framework.serializers import ModelSerializer
from django.db.models import Model, Manager

from .relations import get_manager, retrieve, mutate

def with_relations(func):
  @wraps(func)
  def wrapped(self: 'RelatedSerializer', *args):
    validated_data: dict = args[-1]
    fk_fields, m2m_fields = {}, {}
    if hasattr(self.Meta, 'nested_fields'):
      nested_fields = self.Meta.nested_fields
      fk_fields, m2m_fields = nested_fields.get('one', {}), nested_fields.get('many', {})

    #replace raw data with Model instances
    for field, strategy in fk_fields.items():
      data = validated_data.get(field)
      if data is None:
        continue
      serializer_class: type[ModelSerializer] = type(self.fields[field])

      if strategy == 'retrieve':
        validated_data[field] = retrieve(data, serializer_class)
        continue
      instance_id = data.get('id', '')
      existing = get_manager(serializer_class).get(id=instance_id) if instance_id else None
      validated_data[field] = mutate(existing, data, serializer_class, self.context)

    #we need to extract all m2m fields passed to serializer before create / update and apply the changes latter
    m2m_data_list: dict[str, list[dict]] = {field: validated_data.pop(field, None) for field in m2m_fields}
    instance: Model = func(self, *args)

    #set m2m relationships
    for field, strategy in m2m_fields.items():
      data = m2m_data_list[field]
      if data is None:
        continue
      manager: Manager = getattr(instance, field)
      serializer_class: type[ModelSerializer] = type(self.fields[field].child)

      if strategy == 'retrieve':
        #only m2m models fall in this strategy
        #indeed, when you have a m2m model with ids only, you do need only ids
        manager.set(retrieve(data, serializer_class))
        continue
      mutate(manager.all(), data, serializer_class, self.context)

    instance.save()

    return instance

  return wrapped

class RelatedSerializer(ModelSerializer):
  class Meta:
    nested_fields: dict[str, str]

  @with_relations
  def create(self, validated_data: dict):
    return super().create(validated_data)

  @with_relations
  def update(self, instance: Model, validated_data: dict):
    return super().update(instance, validated_data)