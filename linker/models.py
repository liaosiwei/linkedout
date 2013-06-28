from django.db import models
from django.contrib.auth.models import User

# Create your models here.
    
class Container(models.Model):
    user = models.ForeignKey(User, null=True, blank=True)
    name = models.CharField(max_length=40, null=True, blank=True)
    tags = models.CharField(max_length=100, null=True, blank=True)
    
    def __unicode__(self):
        return u'%s' % self.name
    
class Linker(models.Model):
    container = models.ForeignKey(Container, blank=True, null=True)
    name = models.CharField(max_length=40, null=True, blank=True)
    link = models.CharField(max_length=200, null=True, blank=True)    
    opinion = models.CharField(max_length=400, null=True, blank=True)
    votes = models.IntegerField(default=0)
    date = models.DateTimeField('date created', null=True, blank=True)
    
    def __unicode__(self):
        return u'%s: %s' % (self.name, self.link)
    
