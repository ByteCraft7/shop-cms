from django.db.models.functions import Sign
from django.shortcuts import render
from .utils.email import send_email_otp
import logging
from allauth.account.views import LoginView as OGLoginView
from allauth.account.forms import RequestLoginCodeForm, SignupForm 
from allauth.utils import get_form_class
from allauth.account import app_settings

logger = logging.getLogger("shop.apps.main")

# Create your views here.

class LoginView(OGLoginView):

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['request_code_form'] = RequestLoginCodeForm()
        ctx['signup_form'] = SignupForm()

        return ctx

def home(request):
    context = {}

    return render(request, 'main/index.html', context)

def test(request):
    resp = send_email_otp('arunkakorp@gmail.com', otp='123412', cc=['arun@kumars.io'])
    logger.debug("Got response from send_email_otp:")
    logger.debug(resp)

    return render(request, 'main/index.html')

def fivehundred(request):
    num = 1/0
    return render(request, 'error/500.html')

def not_found(request, exception):
    return render(request, "error/404.html", {}, status=404)

def server_error(request, exception=None):
    return render(request, "error/500.html", {}, status=500)

def unauthorized(request, exception=None):
    return render(request, "error/403.html", {}, status=403)
