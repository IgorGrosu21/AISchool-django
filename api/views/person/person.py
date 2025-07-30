from rest_framework import generics
from drf_spectacular.utils import extend_schema

@extend_schema(tags=['api / person'])
class DetailedPersonView(generics.RetrieveUpdateAPIView):
  @extend_schema(exclude=True)
  def patch(self, request, *args, **kwargs):
    pass