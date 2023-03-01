from django.shortcuts import render, redirect
from .models import ShortURL
import string
import random
from rest_framework.permissions import IsAdminUser
from rest_framework.decorators import api_view, permission_classes
from rest_framework.exceptions import PermissionDenied
from rest_framework.views import exception_handler



@api_view(['GET', 'POST'])
@permission_classes((IsAdminUser, ))
def shorten(request):
    if request.method == 'POST':
        long_url = request.POST['long_url']
        short_code = generate_short_code()  # TODO: Allow user to suggest the shortened string
        short_url = ShortURL(long_url=long_url, short_code=short_code)
        short_url.save()
        return render(request, 'shortener/result.html', {'short_url': request.build_absolute_uri(short_url.short_code)})
    else:
        return render(request, 'shortener/form.html')
    

def generate_short_code(length=6):
    chars = string.ascii_letters + string.digits
    short_code = ''.join(random.choice(chars) for i in range(length))
    return short_code

def redirect_short_url(request, short_code):
    try:
        short_url = ShortURL.objects.get(short_code=short_code)
        return redirect(short_url.long_url)
    except ShortURL.DoesNotExist:
        return render(request, 'shortener/invalid.html')
    
def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)
    if response.status_code == 403:
        return render(context['request'], 'shortener/exceptions/403.html', status=response.status_code)
        # response.status_code = 403
    return response

