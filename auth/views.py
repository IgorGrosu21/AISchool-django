from django.contrib.auth import login
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.exceptions import TokenError
from rest_framework_simplejwt.authentication import JWTAuthentication
from .serializers import AuthUserSerializer
from .models import AuthUser
from .responses import *
from django.core.mail import send_mail
from random import randint

JWT_authenticator = JWTAuthentication()
  
class BaseAuthView(APIView):
  authentication_classes = []
  permission_classes = []
  
  def post(self, request, user):
    login(request, user)
    user.save()
    refresh = RefreshToken.for_user(user)
    user.refresh_token = str(refresh)
    user.save()
    return Succes(refresh.access_token)

class RefreshView(BaseAuthView):
  def post(self, request):
    email = request.data.get('email', None)
    if email:
      user = AuthUser.objects.get(email=email)
      if user.refresh_token:
        refresh = RefreshToken(user.refresh_token)
        try:
          refresh.check_exp()
          return Succes(refresh.access_token)
        except TokenError as e:
          user.refresh_token = None
          user.save()
          print(e)
    return Unauthorized()
  
class SignUpView(BaseAuthView):
  def post(self, request):
    serializer = AuthUserSerializer(data=request.data)
    if not serializer.is_valid():
      return EmailAlreadyRegistered()
  
    user = serializer.save()
    user.set_password(request.data['password'])
    
    return super().post(request, user)

class LogInView(BaseAuthView):
  def post(self, request):
    user = AuthUser.objects.filter(email=request.data['email'])
    if len(user) == 0:
      return UserNotFound()
    
    user = user.first()
    if not user.check_password(request.data['password']):
      return IncorrectPassword()
    
    return super().post(request, user)

class RestoreView(BaseAuthView):
  def post(self, request):
    email = request.data.get('email', None)
    code = request.data.get('code', None)
    password = request.data.get('password', None)
    step = int(request.data.get('step', None))
    print(request.data, request.session.items())
    if step == 1:
      user = AuthUser.objects.filter(email=email)
      if len(user) == 0:
        return UserNotFound()
      
      code = randint(1, 999_999)
      message = f'<h3>Restoring Code for <i>workr.io</i>. <b>Don\'t share this code with anyone!<b></h3><h1>{code}</h1>'
      try:
        send_mail('Password Restoring', '', 'workr.company@gmail.com', [email], False, html_message=message)
      except Exception as e:
        return MailServerError()
      
      user.update(code=code)
      return Succes()
    elif step == 2:
      user = AuthUser.objects.get(email=email)
      if code != user.code:
        return CodeInvalid()
      
      return Succes()
    elif step == 3:
      user = AuthUser.objects.get(email=email)
      user.set_password(password)
      user.code = None
      user.save()
      return super().post(request, user)
    else:
      return Unauthorized()
     
class LogOutView(APIView):
  def post(self, request):
    user = request.user
    user.refresh_token = None
    user.save()
    return Succes()
  
class LogOutAllView(LogOutView):
  def post(self, request):
    request.user.update_key()
    return super().post(request)
  
class UserView(APIView):
  def get(self, request):
    return Response(request.user.email)