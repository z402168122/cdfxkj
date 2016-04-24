# coding=utf-8
from django.shortcuts import render_to_response
from django.contrib import auth
from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.template import RequestContext
from models import HomeBaner
from models import Abouts
from models import Product
from models import ProductType

def home( request, path = '', template_name = "index.html" ):
    blist = HomeBaner.objects.all()
    news = Abouts.objects.filter( ptype = 0 ).order_by( '-id' )[:1]
    plist = Product.objects.filter( recommend = True ).order_by( '-id' )[:4]
    return render_to_response( template_name, locals(), context_instance = RequestContext( request ) )




def product_list( request, product_type = 0, template_name = "list.html" ):
    paths = [['', u'产品中心']]

    pt = ProductType.objects.get( uid = product_type )
    paths.append( [pt.get_url(), pt.name] )
    recs = Product.objects.filter( ptype__uid = product_type ).order_by( '-id' )
    return render_to_response( template_name, locals(), context_instance = RequestContext( request ) )


def product_detail( request, product_type = 0, product_id = 0, template_name = "product_dateil.html" ):

    paths = [['', u'产品中心']]

    rec = Product.objects.get( id = product_id )
    paths.append( [rec.ptype.get_url(), rec.ptype.name ] )
    return render_to_response( template_name, locals(), context_instance = RequestContext( request ) )

def abouts_list( request, about_type = 0, template_name = "abouts_list.html" ):
    paths = [['/abouts', u'关于网硕']]
    if int( about_type ) != -1:
        paths.append( ['/abouts/%s' % about_type, dict( Abouts.ptype_choices ).get( int( about_type ) )] )
    news = Abouts.objects.filter( ptype = 0 ).order_by( '-id' )[:5]
    abouts = Abouts.objects.filter( ptype = 1 ).order_by( '-id' )[:5]

    datas = []
    for k in Abouts.ptype_choices:
        if k[0] == int( about_type ) or about_type == -1:
            recs = Abouts.objects.filter( ptype = k[0] ).order_by( '-id' )
            datas.append( {'name':k[1], 'list':recs} )



    return render_to_response( template_name, locals(), context_instance = RequestContext( request ) )


def abouts_detail( request, about_type = 0, about_id = 0, template_name = "abouts_detail.html" ):
    paths = [['/abouts', u'关于网硕']]
    paths.append( ['/abouts/%s' % about_type, dict( Abouts.ptype_choices ).get( int( about_type ) )] )

    news = Abouts.objects.filter( ptype = 0 ).order_by( '-id' )[:5]
    abouts = Abouts.objects.filter( ptype = 1 ).order_by( '-id' )[:5]

    rec = Abouts.objects.get( id = about_id )

    return render_to_response( template_name, locals(), context_instance = RequestContext( request ) )


