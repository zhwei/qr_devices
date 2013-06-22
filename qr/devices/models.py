#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.db import models

# tinymce
from tinymce.models import HTMLField

class Sorts(models.Model):
    """设备的分类"""

    name = models.CharField(max_length="10", verbose_name="设备分类",  blank=True)

    information = HTMLField(verbose_name="分类描述", blank=True)

    create_date = models.DateField(auto_now_add=True, auto_now=True, blank=True, null=True)


    class Meta:
        verbose_name = "分类"
        verbose_name_plural = "分类"

    def __unicode__(self):
        return self.name

    @models.permalink
    def get_absolute_url(self):
        return ('/sorts/%i' % self.id )


class Devices(models.Model):

    """二维码表"""

    # main information
    name = models.CharField(max_length="20",verbose_name="设备名称" , blank=False)
    location = models.CharField(max_length="50", verbose_name="所在位置", blank=False)


    others = HTMLField(verbose_name="其他信息", blank=True)

    # sorts
    sort = models.ForeignKey(Sorts, verbose_name="设备分类", blank=False)
    model = models.CharField(max_length="50",verbose_name="设备型号", blank=False)
    # sort = models.TextField(verbose_name="设备类别", blank=True)

    # dates

    create_date = models.TimeField(verbose_name="创建日期", auto_now_add=True, blank=True, null=True)
    update_date = models.TimeField(verbose_name="更新日期", auto_now_add=True, auto_now=True,
                                   blank=True, null=True)

    # images

    img = models.ImageField(upload_to="qrcodes", verbose_name="设备二维码",
                            height_field="100", width_field="100", max_length=100,
                            help_text='<p style="color:red;">系统自动生成, 请不要手动修改</p>')
    def get_update_url(self):

        return "/admin/devices/devices/%d/" % self.id

    def qr(self):

        return self.id

    class Meta:
        verbose_name = "设备"
        verbose_name_plural = "设备"

    def __unicode__(self):

        return self.name


    @models.permalink
    def get_absolute_url(self):
        return ('/d/%i' % self.id )
