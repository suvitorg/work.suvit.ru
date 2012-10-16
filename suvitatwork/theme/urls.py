# -*- coding: utf-8 -*-

from django.conf.urls import patterns, include, url
from django.views.generic.base import TemplateView, RedirectView


urlpatterns = patterns('suvitatwork.theme.views',
    url(r'^$',
        TemplateView.as_view(template_name='base.html'),
        name='home'),
    url(r'^support/$',
        'site_support',
        name='support'),
    url(r'^support/browsers/$',
        'support_browsers',
        name='support_browsers'),
    url(r'^support/plans/$',
        'support_plans',
        name='support_plans'),
    url(r'^support/docs/$',
        'support_docs',
        name='support_docs'),
    url(r'^contacts/$',
        TemplateView.as_view(template_name='contacts.html'),
        name='contacts'),

)
