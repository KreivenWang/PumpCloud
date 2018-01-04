# _*_ encoding:utf-8 _*_
from __future__ import unicode_literals
from datetime import datetime

from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.


class UserProfile(AbstractUser):
    birthday = models.DateField(verbose_name=u"生日",null=True,blank=True)
    address = models.CharField(max_length=100,verbose_name=u"地址",default=u"")
    gender = models.CharField(max_length=10,choices=(("male","男"),("female","女")),default=u"",verbose_name=u"性别")
    mobile = models.CharField(max_length=11,null=True,blank=True,verbose_name=u"电话")
    #image = models.FileField(max_length=100,upload_to="image/%Y%m",default=u"image/default.png",verbose_name=u"头像")
    # send_time = models.DateTimeField(default=datetime.now)

    class Meta:
        verbose_name = u"用户信息"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.username


# class EmailVerifyRecord(models.Model):
#     code = models.CharField(max_length=20,verbose_name=u"验证码")
#     email = models.EmailField(max_length=50,verbose_name=u"邮箱")
#     send_time = models.DateTimeField(default=datetime.now,verbose_name=u"时间")
#
#     class Meta:
#         verbose_name = u"邮箱验证"
#         verbose_name_plural = verbose_name
#
#     def __unicode__(self):
#         return '{0}({1})'.format(self.code,self.email)