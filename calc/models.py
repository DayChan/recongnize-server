# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.timezone import now
# Create your models here.

pickname = ["请选择","闯红灯", "压实线", "违章停车"]
class CureData(models.Model):
	
	name = models.CharField('名称', max_length=50)
	file = models.ImageField('图片', upload_to='photos', blank=True)

def __str__(self):
        return self.name