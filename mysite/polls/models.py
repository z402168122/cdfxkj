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
    recommend = models.BooleanField( default = False, verbose_name = u"导航推荐" )
    home_recommend = models.BooleanField( default = False, verbose_name = u"首页推荐" )
    img1 = models.ImageField( u'产品图片' )
    detail1 = models.TextField( verbose_name = "产品特点" , default = '' )
    detail2 = models.TextField( verbose_name = "产品规格", default = '' )
    detail3 = models.TextField( verbose_name = "软件功能" , default = '' )
    detail4 = models.TextField( verbose_name = "典型应用" , default = '' )

    class Meta:
        verbose_name = u'产品'
        verbose_name_plural = '产品'

    def __unicode__( self ):
        return self.name

