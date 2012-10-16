# -*- coding: utf-8 -*-
from django.template import Library

register = Library()

def key(d, key_name):
    return d.get(key_name, '')
key = register.filter('key', key)