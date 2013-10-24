# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Linker'
        db.create_table(u'linker_linker', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=40, null=True, blank=True)),
            ('link', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('tags', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('opinion', self.gf('django.db.models.fields.CharField')(max_length=400, null=True, blank=True)),
            ('votes', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('date', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'linker', ['Linker'])


    def backwards(self, orm):
        # Deleting model 'Linker'
        db.delete_table(u'linker_linker')


    models = {
        u'linker.linker': {
            'Meta': {'object_name': 'Linker'},
            'date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'link': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '40', 'null': 'True', 'blank': 'True'}),
            'opinion': ('django.db.models.fields.CharField', [], {'max_length': '400', 'null': 'True', 'blank': 'True'}),
            'tags': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'votes': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        }
    }

    complete_apps = ['linker']