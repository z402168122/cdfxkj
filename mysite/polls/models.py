# coding=utf-8
from __future__ import unicode_literals

from django.db import models
from mysite import settings

# Create your models here.

class HomeBaner( models.Model ):
    '''
    '''
    img1 = models.ImageField( u'类型图片', default = '' )
    href = models.URLField( u'跳转地址', null = True, blank = True )
    sort_num = models.IntegerField( u'排序', default = 0 )
    create_time = models.DateTimeField( u'创建时间', auto_now = True )

    class Meta:
        verbose_name = u'主页轮播图'
        verbose_name_plural = u'主页轮播图'
        ordering = ['id', '-sort_num']


class ProductType( models.Model ):

    uid = models.IntegerField( u'uid', unique = True, null = True )
    name = models.CharField( u'类型', max_length = 30 )
    img1 = models.ImageField( u'类型图片', null = True )

    class Meta:
        verbose_name = u'产品分类'
        verbose_name_plural = u'产品分类'
        ordering = ['id']

    def __unicode__( self ):
        return self.name

    def get_url( self ):
        return '/products/%s' % self.uid




class Product( models.Model ):

    name = models.CharField( u'名字', max_length = 30 )
    ptype = models.ForeignKey( ProductType, verbose_name = u'类型', default = 0 )
    recommend = models.BooleanField( default = False, verbose_name = u"首页推荐" )
    img = models.ImageField( u'产品图片' )
    detail = models.CharField( u'简单介绍', max_length = 60 , default = '' , blank = True )
    detail1 = models.TextField( verbose_name = "产品特点" , default = '' , blank = True )
    detail2 = models.TextField( verbose_name = "产品规格", default = '' , blank = True )
    detail3 = models.TextField( verbose_name = "软件功能" , default = '' , blank = True )
    detail4 = models.TextField( verbose_name = "典型应用" , default = '' , blank = True )
    detail5 = models.TextField( verbose_name = "订购信息" , default = '' , blank = True )
    create_time = models.DateTimeField( u'创建时间', auto_now = True )

    class Meta:
        verbose_name = u'产品'
        verbose_name_plural = '产品'

    def __unicode__( self ):
        return self.name

    def get_img( self ):
        return '%s/%s' % ( settings.MEDIA_URL, self.img )

    def get_url( self ):
        return '/products/%s/%s.html' % ( self.ptype.id, self.id )



class Abouts( models.Model ):
    ptype_choices = ( ( 0, u'最新资讯' ), ( 1, u'公司介绍' ) )

    title = models.CharField( u'标题', max_length = 30 )
    ptype = models.IntegerField( u'类型', choices = ptype_choices, default = 0 )
    detail = models.TextField( verbose_name = "内容" , default = '' )
    create_time = models.DateTimeField( u'创建时间', auto_now = True )

    class Meta:
        verbose_name = u'关于网硕'
        verbose_name_plural = '关于网硕'

    def __unicode__( self ):
        return self.title

    def get_url( self ):
        return '/abouts/%s/%s.html' % ( self.ptype, self.id )



