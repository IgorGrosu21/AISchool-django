from rest_framework.views import APIView, Response, status
from django.contrib.auth.tokens import default_token_generator
from django.utils.timezone import now
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from auth.models import AuthUser
from core.settings import HOST, EMAIL_HOST_USER

class SendVerificationEmailView(APIView):
  def post(self, request, *args, **kwargs):
    user = request.user
    if user.is_verified:
      return Response({'error': 'already_verified'}, status=status.HTTP_400_BAD_REQUEST)

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
  
  def get(self, request):
    pk = request.query_params.get('pk')
    token = request.query_params.get('token')

    try:
      user = AuthUser.objects.get(pk=pk)
    except AuthUser.DoesNotExist:
      return Response({'error': 'user_doesnt_exist'}, status=status.HTTP_400_BAD_REQUEST)

    if default_token_generator.check_token(user, token):
      user.is_verified = True
      user.save()
      return Response(None, status=status.HTTP_204_NO_CONTENT)
    else:
      return Response({'error': 'invalid_token'}, status=status.HTTP_400_BAD_REQUEST)