# coding=utf-8
from django.contrib import admin


from models import ProductType, Product

# Register your models here.

admin.site.register( ProductType )



# Register your models here.

@admin.register( Product )
class ArticleAdmin( admin.ModelAdmin ):

    list_display = ( 'name', )

    class Media:
        # 在管理后台的HTML文件中加入js文件, 每一个路径都会追加STATIC_URL/
        js = ( 
            'js/kindeditor/kindeditor-all.js',
            # 'js/kindeditor/lang.zh_CN.js',
             'js/kindeditor/config.js',
        )
