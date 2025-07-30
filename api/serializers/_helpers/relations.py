from rest_framework.serializers import ModelSerializer
from django.db.models import Model, Manager, QuerySet

def get_manager(cls: type[ModelSerializer]) -> Manager:
  return cls.Meta.model.objects

def extract_id(validated_data: dict) -> str:
  return validated_data.get('id', '')

def extract_ids(validated_data_list: list[dict]) -> list[str]:
  return [entry.get('id') for entry in validated_data_list if entry.get('id', '') != '']



def retrieve(validated_data: dict | list[dict], serializer_class: type[ModelSerializer]):
  manager = get_manager(serializer_class)
  if isinstance(validated_data, list):
    return manager.filter(id__in=extract_ids(validated_data))
  return manager.get(id=extract_id(validated_data))



def mutate(existing: Model | QuerySet | None, validated_data: dict | list[dict], serializer_class: type[ModelSerializer], context: dict):
  serializer_class_with_context = lambda *args, **kwargs: serializer_class(*args, **kwargs, context=context)
  
  if isinstance(existing, QuerySet):
    return mutate_many(existing, validated_data, serializer_class_with_context)
  validated_data.pop('id', None)
  return mutate_one(existing, validated_data, serializer_class_with_context)

def mutate_one(existing: Model | None, validated_data: dict, serializer_class: type[ModelSerializer]):
  for key, value in validated_data.items():
    if isinstance(value, Model):
      validated_data[key] = value.id
  serializer = serializer_class(existing, data=validated_data)
  serializer.is_valid(raise_exception=True)
  return serializer.save()

def mutate_many(existing_qs: QuerySet, validated_data_list: list[dict], serializer_class: type[ModelSerializer]):
  incoming_ids = extract_ids(validated_data_list)
  existing_qs.exclude(id__in=incoming_ids).delete()
  
  existing_ids = {str(entry.id): entry for entry in existing_qs}
  
  instances = []
  for entry in validated_data_list:
    entry_id = str(entry.get('id', '')).strip()

    if entry_id and entry_id in existing_ids:
      existing = existing_ids[entry_id]
      instances.append(mutate_one(existing, entry, serializer_class))
      continue
    entry.pop('id', None)
    instances.append(mutate_one(None, entry, serializer_class))