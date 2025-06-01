from rest_framework import status
from rest_framework.views import APIView, Response

from api.models import Media, User, Student, Teacher
from api.serializers import DetailedUserSerializer, MediaSerializer

class UserView(APIView):
  queryset = User.objects.all()
  serializer_class = DetailedUserSerializer
  
  def get(self, request, *args, **kwargs):
    user = request.user.user
    serializer = self.serializer_class(user, context={'request': request})
    return Response(serializer.data, status=status.HTTP_200_OK)

  def post(self, request, *args, **kwargs):
    user, created = User.objects.get_or_create(account=request.user)
    data = request.data
    data.pop('id')
    serializer = self.serializer_class(user, data=data)
    if serializer.is_valid():
      user = serializer.save()
      if user.is_teacher:
        if created or not Teacher.objects.filter(user=user).exists():
          Teacher.objects.create(user=user)
      else:
        if created or not Student.objects.filter(user=user).exists():
          Student.objects.create(user=user)
      serializer = self.serializer_class(user)
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    print(serializer.errors)
    if created:
      user.delete()
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  
  def patch(self, request, *args, **kwargs):
    user = request.user.user
    if not user.avatar:
      serializer = MediaSerializer(data=request.data)
      if serializer.is_valid():
        avatar = serializer.validated_data.get('file')
        user.avatar = avatar
        user.save()
        return Response(Media.append_prefix(user.avatar.name), status=status.HTTP_201_CREATED)
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    serializer = MediaSerializer(user.avatar, data=request.data)
    if serializer.is_valid():
      avatar = serializer.validated_data.get('file')
      user.avatar = avatar
      user.save()
      return Response(Media.append_prefix(user.avatar.name), status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  
  def delete(self, request, *args, **kwargs):
    user = request.user.user
    user.avatar.delete()
    return Response(None, status=status.HTTP_204_NO_CONTENT)
      