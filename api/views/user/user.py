from rest_framework import status, generics
from rest_framework.views import APIView, Response

from api.models import User, Student, Teacher
from api.serializers import DetailedUserSerializer, UserRoutesSerializer, MediaSerializer

class DetailedUserView(APIView):
  queryset = User.objects.all()
  serializer_class = DetailedUserSerializer
  
  def get(self, request, *args, **kwargs):
    user: User = request.user.user
    serializer = self.serializer_class(user, context={'request': request})
    return Response(serializer.data, status=status.HTTP_200_OK)

  def post(self, request, *args, **kwargs):
    user, created = User.objects.get_or_create(account=request.user)
    data = request.data
    data.pop('id')
    is_teacher = data.pop('is_teacher')
    serializer = self.serializer_class(user, data=data)
    if serializer.is_valid():
      user = serializer.save()
      manager = Teacher.objects if is_teacher else Student.objects
      if is_teacher:
        if created or not manager.filter(user=user).exists():
          manager.create(user=user)
      else:
        if created or not manager.filter(user=user).exists():
          manager.create(user=user)
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    if created:
      user.delete()
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  
  def patch(self, request, *args, **kwargs):
    user: User = request.user.user
    serializer = MediaSerializer(user.avatar, data=request.data)
    if serializer.is_valid():
      avatar = serializer.validated_data.get('file')
      user.avatar = avatar
      user.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  
  def delete(self, request, *args, **kwargs):
    user = request.user.user
    user.avatar.delete()
    return Response(None, status=status.HTTP_204_NO_CONTENT)
  
class UserRoutesView(generics.RetrieveAPIView):
  queryset = User.objects.all()
  serializer_class = UserRoutesSerializer
  
  def get_object(self) -> User:
    return self.request.user.user