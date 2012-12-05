from django.contrib import admin
from suvitatwork.theme.models import Client, Service, Project, Work

admin.site.register(Client)
admin.site.register(Service)
admin.site.register(Project)
admin.site.register(Work)