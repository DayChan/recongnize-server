# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.timezone import now
# Create your models here.

class CureData(models.Model):
	name = models.CharField('名称', max_length=50)
	file = models.ImageField('图片', upload_to='photos', blank=True)

def __unicode__(self):
        return self.name