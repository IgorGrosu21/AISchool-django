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
  return mutate_one(existing, validated_data, serializer_class_with_context)

def mutate_one(existing: Model | None, validated_data: dict, serializer_class: type[ModelSerializer]):
  for key, value in validated_data.items():
    if isinstance(value, Model):
      validated_data[key] = value.id
  if existing:
    serializer = serializer_class(existing, data=validated_data)
  else:
    validated_data.pop('id', None)
    serializer = serializer_class(data=validated_data)
  if serializer.is_valid():
    return serializer.save()
  return existing

def mutate_many(existing: QuerySet, validated_data_list: list[dict], serializer_class: type[ModelSerializer]):
  def find_data(entry_id: str):
    entry_id = str(entry_id)
    for data in validated_data_list:
      if str(data.get('id')) == entry_id:
        return data
    return None

  ids = extract_ids(validated_data_list)
  to_delete_list = existing.exclude(id__in=ids)
  to_create_list = [entry for entry in validated_data_list if entry.get('id') == '']
  to_update_list = {entry: find_data(entry.id) for entry in existing.filter(id__in=ids)}
  
  to_delete_list.delete()
  
  instances = []
  for to_create in to_create_list:
    instances.append(mutate_one(None, to_create, serializer_class))
  for entry, to_update in to_update_list.items():
    instances.append(mutate_one(entry, to_update, serializer_class))
  
  return instances