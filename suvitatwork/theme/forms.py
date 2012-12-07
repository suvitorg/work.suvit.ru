# -*- coding: utf-8 -*-
from django import forms


class SmsForm(forms.Form):
    message = forms.CharField(u"Сообщение", widget=forms.Textarea)