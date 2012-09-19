# Create your views here.
from django.template.response import TemplateResponse

def main(request):
    return TemplateResponse(request, 'base.html',
                            {})

def site_support(request):
    return TemplateResponse(request, 'support/base.html',
                            {})

def support_browsers(request):
    return TemplateResponse(request, 'support/browsers.html',
                            {})

