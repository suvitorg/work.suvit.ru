# Create your views here.
from django.conf import settings
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

def support_plans(request):
    return TemplateResponse(request, 'support/plans.html',
                            {'plans': settings.PLANS,
                             'features': settings.PLAN_FEATURES})

def support_docs(request):
    return TemplateResponse(request, 'support/docs.html',
                            {})
