# coding=utf-8
from django.shortcuts import render_to_response
from django.contrib import auth
from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.template import RequestContext
from models import HomeBaner
from models import Abouts
from models import Product
from models import ProductType
import json
from mysite import settings


def home( request, path = '', template_name = "index.html" ):
    blist = HomeBaner.objects.all()
    news = Abouts.objects.filter( ptype = 0 ).order_by( '-id' )[:1]
    plist = Product.objects.filter( recommend = True ).order_by( '-id' )[:4]
    return render_to_response( template_name, locals(), context_instance = RequestContext( request ) )


def update_img( request ):
    import os
    import time
    import random
    if not request.user.is_authenticated:
        raise Http404

    f = request.FILES['imgFile']

    ext = os.path.splitext( f.name )[1]

    fn = time.strftime( '%Y%m%d%H%M%S' )
    fn = fn + '_%d' % random.randint( 0, 100 )

    # 重写合成文件名
    name = fn + ext
    path = os.path.join( settings.MEDIA_ROOT, name )

    path = path.encode( 'gbk' )
    destination = open( path, 'wb+' )
    for chunk in f.chunks():
        destination.write( chunk )
    destination.close()

    data = {
            "error" : 0,
            "url" :  settings.MEDIA_URL + '/' + name
    }
    return HttpResponse( json.dumps( data ) )



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


from models import Supports
def supports_list( request, vtype = 0, template_name = "supports_list.html" ):
    paths = [['/supports', u'服务支持']]
    if int( vtype ) != -1:
        paths.append( ['/supports/%s' % vtype, dict( Supports.ptype_choices ).get( int( vtype ) )] )
    news = Supports.objects.filter( ptype = 0 ).order_by( '-id' )[:5]
    abouts = Supports.objects.filter( ptype = 1 ).order_by( '-id' )[:5]

    datas = []
    for k in Supports.ptype_choices:
        if k[0] == int( vtype ) or vtype == -1:
            recs = Supports.objects.filter( ptype = k[0] ).order_by( '-id' )
            datas.append( {'name':k[1], 'list':recs} )



    return render_to_response( template_name, locals(), context_instance = RequestContext( request ) )


def supports_detail( request, vtype = 0, vid = 0, template_name = "supports_dateil.html" ):
    paths = [['/supports', u'服务支持']]
    paths.append( ['/supports/%s' % vtype, dict( Supports.ptype_choices ).get( int( vtype ) )] )

    news = Supports.objects.filter( ptype = 0 ).order_by( '-id' )[:5]
    abouts = Supports.objects.filter( ptype = 1 ).order_by( '-id' )[:5]

    rec = Supports.objects.get( id = vid )

    return render_to_response( template_name, locals(), context_instance = RequestContext( request ) )



from models import Solution
from models import SolutionType
def solutions_list( request, vtype = 0, template_name = "solutions_list.html" ):
    if int( vtype ) == -1:
        st = SolutionType.objects.all()[:1]
        if st:
            return HttpResponseRedirect( '/solutions/%s' % st[0].id )
        else:
            raise Http404
    st = SolutionType.objects.get( id = vtype )

    paths = [['', u'解决方案']]
    if int( vtype ) != -1:
        paths.append( ['/solutions/%s' % vtype, st.name] )

    news = Solution.objects.filter( ptype = 0 ).order_by( '-id' )[:5]
    abouts = Solution.objects.filter( ptype = 1 ).order_by( '-id' )[:5]

    datas = []
    for k in [st]:
        recs = Solution.objects.filter( ptype = k ).order_by( '-id' )
        datas.append( {'name':st.name, 'list':recs} )



    return render_to_response( template_name, locals(), context_instance = RequestContext( request ) )


def solutions_detail( request, vtype = 0, vid = 0, template_name = "solutions_dateil.html" ):
    paths = [['', u'解决方案']]
    st = SolutionType.objects.get( id = vtype )
    paths.append( ['/solutions/%s' % vtype, st.name] )

    news = Solution.objects.filter( ptype = 0 ).order_by( '-id' )[:5]
    abouts = Solution.objects.filter( ptype = 1 ).order_by( '-id' )[:5]

    rec = Solution.objects.get( id = vid )

    return render_to_response( template_name, locals(), context_instance = RequestContext( request ) )




