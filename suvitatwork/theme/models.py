from django.contrib.auth.models import User
from django.db import models

from userena.models import UserenaLanguageBaseProfile


class MyProfile(UserenaLanguageBaseProfile):
    user = models.OneToOneField(User,
                                unique=True,
                                verbose_name='User',
                                related_name='my_profile')

