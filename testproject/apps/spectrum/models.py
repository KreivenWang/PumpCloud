# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class InferComboReport(models.Model):
    DisplayText = models.CharField(max_length=50,verbose_name=u"故障描述")
    CompCode = models.CharField(max_length=100,verbose_name=u"故障设备编号")
    RtDatas = models.CharField(max_length=100,verbose_name=u"故障出现的频谱图位置")

    class Meta:
        verbose_name = u"故障"
        verbose_name_plural = verbose_name
        db_table = 'InferComboReport'

    def __unicode__(self):
        return self.CompCode


