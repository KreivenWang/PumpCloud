# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class InferComboReport(models.Model):
    Id = models.IntegerField(verbose_name=u"编号")
    DisplayText = models.CharField(max_length=50,verbose_name=u"故障描述")
    CompCode = models.CharField(max_length=100,verbose_name=u"故障设备编号")
    RtDatas = models.CharField(max_length=100,verbose_name=u"故障出现的频谱图位置")
    RRId = models.IntegerField(verbose_name=u"运行次数")

    class Meta:
        verbose_name = u"组合推断报告"
        verbose_name_plural = verbose_name
        db_table = 'InferComboReport'

    def __unicode__(self):
        return self.CompCode


class GraphArchives(models.Model):
    Id = models.IntegerField(verbose_name=u"编号")
    DataStr = models.CharField(max_length=100000, verbose_name=u"数据1")
    FeatureStr = models.CharField(max_length=100000, verbose_name=u"数据2")
    class Meta:
        verbose_name = u"频谱图"
        verbose_name_plural = verbose_name
        db_table = 'GraphArchives'


class FaultItemReport(models.Model):
    GraphMap = models.CharField(max_length=100000, verbose_name=u"对应频谱")
    CriterionBuiltIds = models.CharField(max_length=100000, verbose_name=u"判据构建ID")
    CompCode = models.CharField(max_length=50, verbose_name=u"故障设备编号")
    RRId = models.IntegerField(verbose_name=u"运行次数")

    class Meta:
        verbose_name = u"故障顶报告"
        verbose_name_plural = verbose_name
        db_table = 'FaultItemReport'