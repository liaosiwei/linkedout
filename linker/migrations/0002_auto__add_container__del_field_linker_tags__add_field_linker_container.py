# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Container'
        db.create_table(u'linker_container', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=40, null=True, blank=True)),
            ('tags', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
        ))
        db.send_create_signal(u'linker', ['Container'])

        # Deleting field 'Linker.tags'
        db.delete_column(u'linker_linker', 'tags')

        # Adding field 'Linker.container'
        db.add_column(u'linker_linker', 'container',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['linker.Container'], null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting model 'Container'
        db.delete_table(u'linker_container')

        # Adding field 'Linker.tags'
        db.add_column(u'linker_linker', 'tags',
                      self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True),
                      keep_default=False)

        # Deleting field 'Linker.container'
        db.delete_column(u'linker_linker', 'container_id')


    models = {
        u'linker.container': {
            'Meta': {'object_name': 'Container'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '40', 'null': 'True', 'blank': 'True'}),
            'tags': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'})
        },
        u'linker.linker': {
            'Meta': {'object_name': 'Linker'},
            'container': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['linker.Container']", 'null': 'True', 'blank': 'True'}),
            'date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'link': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '40', 'null': 'True', 'blank': 'True'}),
            'opinion': ('django.db.models.fields.CharField', [], {'max_length': '400', 'null': 'True', 'blank': 'True'}),
            'votes': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        }
    }

    complete_apps = ['linker']