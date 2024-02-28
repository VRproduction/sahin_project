from .models import *
import datetime

def extras(request):
    context={
        'current_year': datetime.datetime.now().year,
        'setting': GeneralSettings.objects.first(),
        
    }
    is_mobile = False
    user_agent = request.META.get('HTTP_USER_AGENT', '').lower()
    if 'mobile' in user_agent or 'android' in user_agent or 'iphone' in user_agent:
        is_mobile = True
    context["is_mobile"] = is_mobile
    return context