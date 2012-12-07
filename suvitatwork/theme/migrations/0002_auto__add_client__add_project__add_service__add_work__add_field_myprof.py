# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Client'
        db.create_table('theme_client', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(related_name='clients', to=orm['auth.User'])),
        ))
        db.send_create_signal('theme', ['Client'])

        # Adding model 'Project'
        db.create_table('theme_project', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('repository', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('client', self.gf('django.db.models.fields.related.ForeignKey')(related_name='projects', to=orm['theme.Client'])),
        ))
        db.send_create_signal('theme', ['Project'])

        # Adding model 'Service'
        db.create_table('theme_service', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('price', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal('theme', ['Service'])

        # Adding M2M table for field clients on 'Service'
        db.create_table('theme_service_clients', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('service', models.ForeignKey(orm['theme.service'], null=False)),
            ('client', models.ForeignKey(orm['theme.client'], null=False))
        ))
        db.create_unique('theme_service_clients', ['service_id', 'client_id'])

        # Adding model 'Work'
        db.create_table('theme_work', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('executor', self.gf('django.db.models.fields.related.ForeignKey')(related_name='works', to=orm['auth.User'])),
            ('work_costs', self.gf('django.db.models.fields.DecimalField')(default='0', max_digits=10, decimal_places=2)),
        ))
        db.send_create_signal('theme', ['Work'])

        # Adding field 'MyProfile.phone'
        db.add_column('theme_myprofile', 'phone',
                      self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting model 'Client'
        db.delete_table('theme_client')

        # Deleting model 'Project'
        db.delete_table('theme_project')

        # Deleting model 'Service'
        db.delete_table('theme_service')

        # Removing M2M table for field clients on 'Service'
        db.delete_table('theme_service_clients')

        # Deleting model 'Work'
        db.delete_table('theme_work')

        # Deleting field 'MyProfile.phone'
        db.delete_column('theme_myprofile', 'phone')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'theme.client': {
            'Meta': {'object_name': 'Client'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'clients'", 'to': "orm['auth.User']"})
        },
        'theme.myprofile': {
            'Meta': {'object_name': 'MyProfile'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.CharField', [], {'default': "'ru'", 'max_length': '5'}),
            'mugshot': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'privacy': ('django.db.models.fields.CharField', [], {'default': "'registered'", 'max_length': '15'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'my_profile'", 'unique': 'True', 'to': "orm['auth.User']"})
        },
        'theme.project': {
            'Meta': {'object_name': 'Project'},
            'client': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'projects'", 'to': "orm['theme.Client']"}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'repository': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '150'})
        },
        'theme.service': {
            'Meta': {'object_name': 'Service'},
            'clients': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'services'", 'symmetrical': 'False', 'to': "orm['theme.Client']"}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'price': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '150'})
        },
        'theme.work': {
            'Meta': {'object_name': 'Work'},
            'description': ('django.db.models.fields.TextField', [], {}),
            'executor': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'works'", 'to': "orm['auth.User']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'work_costs': ('django.db.models.fields.DecimalField', [], {'default': "'0'", 'max_digits': '10', 'decimal_places': '2'})
        }
    }

    complete_apps = ['theme']