# coding=utf-8
from django.contrib import admin


from models import ProductType, Product

from models import HomeBaner, Abouts
from models import Supports
from models import Solution, SolutionType


@admin.register( HomeBaner )
class HomeBanerAdmin( admin.ModelAdmin ):
    list_display = ( 'id', 'img1', 'sort_num', 'create_time' )



@admin.register( ProductType )
class ProductTypeAdmin( admin.ModelAdmin ):

    list_display = ( 'id', 'uid', 'name' )



# Register your models here.

@admin.register( Product )
class ProductAdmin( admin.ModelAdmin ):

    list_display = ( 'name', 'recommend', 'detail', 'create_time' )

    class Media:
        # 在管理后台的HTML文件中加入js文件, 每一个路径都会追加STATIC_URL/
        js = ( 
            'js/kindeditor/kindeditor-all.js',
            # 'js/kindeditor/lang.zh_CN.js',
             'js/kindeditor/config.js',
        )


@admin.register( SolutionType )
class SolutionTypeAdmin( admin.ModelAdmin ):

    list_display = ( 'id', 'uid', 'name' )



# Register your models here.

@admin.register( Solution )
class SolutionAdmin( admin.ModelAdmin ):

    list_display = ( 'name', 'create_time' )

    class Media:
        # 在管理后台的HTML文件中加入js文件, 每一个路径都会追加STATIC_URL/
        js = ( 
            'js/kindeditor/kindeditor-all.js',
            # 'js/kindeditor/lang.zh_CN.js',
             'js/kindeditor/config1.js',
        )

@admin.register( Supports )
class SupportsAdmin( admin.ModelAdmin ):
    list_display = ( 'id', 'title', 'ptype', 'create_time' )

    class Media:
        # 在管理后台的HTML文件中加入js文件, 每一个路径都会追加STATIC_URL/
        js = ( 
            'js/kindeditor/kindeditor-all.js',
            # 'js/kindeditor/lang.zh_CN.js',
             'js/kindeditor/config1.js',
        )


@admin.register( Abouts )
class AboutsAdmin( admin.ModelAdmin ):
    list_display = ( 'id', 'title', 'ptype', 'create_time' )
    class Media:
        # 在管理后台的HTML文件中加入js文件, 每一个路径都会追加STATIC_URL/
        js = ( 
            'js/kindeditor/kindeditor-all.js',
            # 'js/kindeditor/lang.zh_CN.js',
             'js/kindeditor/config1.js',
        )
