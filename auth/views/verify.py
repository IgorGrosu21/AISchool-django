from rest_framework.views import APIView, Response, Request, status
from rest_framework.exceptions import ParseError, NotFound
from rest_framework.throttling import AnonRateThrottle
from django.contrib.auth.tokens import default_token_generator
from django.utils.timezone import now
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from drf_spectacular.utils import extend_schema

from core.settings import HOST, EMAIL_HOST_USER
from auth.models import AuthUser

class SendVerificationEmailView(APIView):
  @extend_schema(tags=['auth / verify'], request=None, responses={
    status.HTTP_204_NO_CONTENT: None
  })
  def post(self, request: Request, *args, **kwargs):
    user: AuthUser = request.user
    if user.is_verified:
      raise ParseError(code='already_verified')

    token = default_token_generator.make_token(user)
    verify_link = f'{HOST}/auth/verify/?pk={user.pk}&token={token}'

    context = {
      'username': f'{user.user.name} {user.user.surname}',
      'verify_url': verify_link,
      'now': now(),
    }

    html_content = render_to_string('verify_email.html', context)
    text_content = strip_tags(html_content)

    email = EmailMultiAlternatives(
      subject='Подтвердите свой аккаунт',
      body=text_content,
      from_email=EMAIL_HOST_USER,
      to=['igrgro@gmail.com']#[user.email],
    )
    email.attach_alternative(html_content, 'text/html')
    email.send()

    return Response(None, status=status.HTTP_204_NO_CONTENT)

class VerifyDetailedUserView(APIView):
  authentication_classes = []
  permission_classes = []
  throttle_classes = [AnonRateThrottle]
  
  @extend_schema(tags=['auth / verify'], request=None, responses={
    status.HTTP_204_NO_CONTENT: None
  })
  def get(self, request: Request):
    pk = request.query_params.get('pk', None)
    token = request.query_params.get('token', None)

    try:
      user = AuthUser.objects.get(pk=pk)
    except AuthUser.DoesNotExist:
      raise NotFound(code='user_doesn\'t_exist')

    if default_token_generator.check_token(user, token):
      user.is_verified = True
      user.save()
      return Response(None, status=status.HTTP_204_NO_CONTENT)
    raise ParseError(code='incorrect_token')