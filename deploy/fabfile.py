# -*- coding: utf-8 -*-
from datetime import datetime
import os
import sys

import fabric.api as fab

from speedydeploy.base import Debian
from speedydeploy.deployment import _, Deployment
from speedydeploy.database import SqliteDatabase, Maria53Database
from speedydeploy.vcs import GIT
from speedydeploy.project import Project, Memcache, CronTab
from speedydeploy.server import FcgiWrapper
from speedydeploy.project.django import Django14

class SuvitWorkDeployment(Deployment):

    def node2(self):
        fab.env.hosts = ["node2.suvit.ru"]
        fab.env.user = "u24337"

        fab.env.project_name = "work.suvit.ru/suvitatwork"
        fab.env.instance_name = fab.env.user
        fab.env.remote_dir = _("/home/%(user)s/%(project_name)s/")

        fab.env.os = Debian()

        fab.env.db = SqliteDatabase()

        fab.env.project = Project()
        fab.env.project.django = fab.env.django = Django14(_('%(remote_dir)s/%(project_name)s/'),
                                                  settings_local=_('settings/settings_prod.py'),
                                                  python_path=_('%(remote_dir)s/env/bin/python'))
        fab.env.project.django.USE_STATICFILES = True
        fab.env.project.django.USE_SOUTH = False

        fab.env.server = FcgiWrapper(domain='work.suvit.ru')

        fab.env.vcs = GIT()
        fab.env.git_path = \
            'https://github.com/suvitorg/work.suvit.ru'

        fab.env.cron = CronTab()

    def install(self, key=None):
        #self.ssh_add_key(key or "C:/bin/key")
        self.create_env()
        self.deploy()
        self.update_virtual_env()

    def update_code(self):
        project = fab.env.project

        if project.use_django:
            project.django.reload()

        if project.use_celery:
            self.celery_configure()
        if project.use_sphinxsearch:
            self.sphinxsearch_configure()
        if project.use_memcache:
            self.memcache_configure()

        if project.use_server:
            self.server_configure()
            #self.server_restart()
            self.server_reload()

    def update(self):
        self.vcs_deploy()
        self.update_code()
        self.test_data()

    def test_data(self):
        pass

    def update_cron(self):

        context = dict(python_path=_('%(remote_dir)s/env/bin/python'),
                       manage_path=_('%(remote_dir)s/koesanshop/manage.py'),
                       project_path=_('%(remote_dir)s'),
                       log_path=_('%(remote_dir)s/log')
                      )

        crontab = fab.env.cron

        crontab.update('*/5 * * * * %(python_path)s %(manage_path)s send_mail' % context,
                       marker='send_mail')


instance = SuvitWorkDeployment()
