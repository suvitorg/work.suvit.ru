# -*- coding: utf-8 -*-
from django.contrib import admin
from django.shortcuts import get_object_or_404, render
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.utils.functional import update_wrapper

from suvitatwork.theme.models import Client, Service, Project, Work, MyProfile
from suvitatwork.theme.forms import SmsForm

from sendsms.message import SmsMessage

admin.site.register(Service)
admin.site.register(Project)
admin.site.register(Work)



class ClientAdmin(admin.ModelAdmin):

    def send_sms(self, request, object_id):
        client = get_object_or_404(Client, pk=object_id)
        profile = client.user.get_profile()
        phone = profile.phone
        form = SmsForm(data=request.POST or None)
        if request.method == 'POST' and form.is_valid() and phone:
            SmsMessage(form.cleaned_data['message'], to=phone).send()
            messages.add_message(request, messages.INFO, u"Сообщение отправлено")
            return HttpResponseRedirect('..')

        return render(request,
                      'admin/theme/client/send_sms.html',
                      {'form': form,
                       'profile': profile,
                       'opts': self.model._meta,
                       'profile_opts': MyProfile._meta,
                       'object_id': object_id,
                       'has_change_permission': self.has_change_permission(request, None),
                       'app_label': self.model._meta.app_label})

    def get_urls(self):
        from django.conf.urls.defaults import patterns, url

        def wrap(view):
            def wrapper(*args, **kwargs):
                return self.admin_site.admin_view(view)(*args, **kwargs)
            return update_wrapper(wrapper, view)

        info = self.model._meta.app_label, self.model._meta.module_name

        urls = patterns('',
            url(r'^(.+)/send_sms/$',
                wrap(self.send_sms),
                name='%s_%s_send_sms' % info),
        )

        urls += super(ClientAdmin, self).get_urls()

        return urls

admin.site.register(Client, ClientAdmin)


