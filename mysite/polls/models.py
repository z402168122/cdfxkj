# coding=utf-8
from __future__ import unicode_literals

from django.db import models

# Create your models here.




class ProductType( models.Model ):

    name = models.CharField( u'类型', max_length = 30 )

    class Meta:
        verbose_name = u'产品分类'
        verbose_name_plural = u'产品分类'

    def __unicode__( self ):
        return self.name




class Product( models.Model ):

    name = models.CharField( u'名字', max_length = 30 )
    ptype = models.ForeignKey( ProductType, verbose_name = u'类型' )
    img1 = models.ImageField( u'图片' )
    detail1 = models.TextField( u'产品概览' )
    detail2 = models.TextField( u'详细参数' )
    detail3 = models.TextField( u'资料下载' )
    detail4 = models.TextField( u'产品演示' )

    class Meta:
        verbose_name = u'产品'
        verbose_name_plural = '产品'

    def __unicode__( self ):
        return self.name


