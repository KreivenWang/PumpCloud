# _*_ encoding:utf-8 _*_
from __future__ import unicode_literals
import datetime

from django.db import models

# Create your models here.


class Company(models.Model):
    name = models.CharField(max_length=50,verbose_name=u"名称")
    address = models.CharField(max_length=100,verbose_name=u"地址")

    class Meta:
        verbose_name = u"水司"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name


class Station(models.Model):
    company = models.ForeignKey(Company,verbose_name=u"隶属水司")
    name = models.CharField(max_length=50,verbose_name=u"名称")
    address = models.CharField(max_length=100,verbose_name=u"地址")
    longitude = models.FloatField(blank=True,verbose_name=u"经度",default=0)
    latitude = models.FloatField(blank=True,verbose_name=u"纬度",default=0)
    contact = models.CharField(blank=True,max_length=50,verbose_name=u"联系方式")
    image = models.ImageField(upload_to="station/%Y/%m",max_length=50,verbose_name=u"图片", null=True, blank=True)

    class Meta:
        verbose_name = u"泵站"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name


class Pump(models.Model):
    station = models.ForeignKey(Station, verbose_name=u"隶属泵站")
    name = models.CharField(max_length=50, verbose_name=u"机组名称")
    pumpcode = models.CharField(max_length=50, verbose_name=u"编号")
    pumpPublishCode = models.CharField(max_length=50, verbose_name=u"水泵出厂编号",default='')
    pumpPublishDate = models.DateField(verbose_name=u"水泵出厂日期",default=datetime.date.today)
    motorPublishCode = models.CharField(max_length=50, verbose_name=u"电机出厂编号",default='')
    motorPublishDate = models.DateField(verbose_name=u"电机出厂日期",default=datetime.date.today)
    beginUseDate = models.DateField(verbose_name=u"投入使用时间",default=datetime.date.today)
    pumpProductType = models.CharField(max_length=50, verbose_name=u"水泵型号",default='')
    motorProductType = models.CharField(max_length=50, verbose_name=u"电机型号",default='')


    status = models.CharField(choices=(("online", u"在线"), ("offline", u"离线")), max_length=8, verbose_name=u"状态")
    # running = models.BooleanField(verbose_name=u"是否运行")


    class Meta:
        verbose_name = u"机泵"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name


# class Spectrum(models.Model):
#     pump = models.ForeignKey(Pump,verbose_name=u"隶属机泵")
#     num = models.IntegerField(verbose_name=u"编号")
#     data = models.CharField(max_length=2000, verbose_name=u"数据")
#     datetime = models.DateTimeField(verbose_name=u"时间")
#     local = models.CharField(max_length=50, verbose_name=u"位置")
#
#     class Meta:
#         verbose_name = u"频谱"
#         verbose_name_plural = verbose_name
#
#     def __unicode__(self):
#         return self.num
