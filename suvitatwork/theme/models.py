# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from django.db import models

from userena.models import UserenaLanguageBaseProfile


class MyProfile(UserenaLanguageBaseProfile):
    user = models.OneToOneField(User,
                                unique=True,
                                verbose_name='User',
                                related_name='my_profile')
    phone = models.CharField(u"Телефон",
                             max_length=100,
                             null=True, blank=True)

class Client(models.Model):
    title = models.CharField(u"Название",
                             max_length=150)
    user = models.ForeignKey(User,
                             verbose_name=u"Пользователь",
                             related_name='clients')


class Service(models.Model):
    title = models.CharField(u"Название",
                             max_length=150)
    description = models.TextField(u"Описание",
                                   null=True, blank=True)
    price = models.CharField(u"Цена",
                             max_length=100)
    clients = models.ManyToManyField(Client,
                                     verbose_name=u"Клиенты",
                                     related_name='services')


class Project(models.Model):
    title = models.CharField(u"Название",
                             max_length=150)
    description = models.TextField(u"Описание",
                                   null=True, blank=True)
    repository = models.CharField(u"Репозитарий",
                                  max_length=150)
    client = models.ForeignKey(Client,
                               verbose_name=u"Клиент",
                               related_name='projects')


class Work(models.Model):
    description = models.TextField(u"Описание")

    executor = models.ForeignKey(User,
                                 verbose_name=u"Исполнитель",
                                 related_name='works')
    work_costs = models.DecimalField(u"Трудозатраты",
                                     max_digits=10,
                                     decimal_places=2,
                                     default='0')
