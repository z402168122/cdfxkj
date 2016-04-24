# coding=utf-8

from models import ProductType
from models import Product
from models import Abouts
from models import Supports
from models import Solution
from models import SolutionType


def header( request ):    # context处理器
    product_header = {}
    product_list_header = {}
    pts = ProductType.objects.all()
    for p in pts:
        product_header[p.uid] = p
        recs = Product.objects.filter( ptype = p ).order_by( '-id' )[:5]
        product_list_header[p.uid] = recs

    data = {'product_header':product_header, 'product_list_header':product_list_header}

    abouts_list_header = {}
    recs = Abouts.objects.filter( ptype = 0 ).order_by( '-id' )[:5]
    abouts_list_header[0] = recs
    recs = Abouts.objects.filter( ptype = 1 ).order_by( '-id' )[:5]
    abouts_list_header[1] = recs
    data['abouts_list_header'] = abouts_list_header

    supports_list_head = {}
    recs = Supports.objects.filter( ptype = 0 ).order_by( '-id' )[:5]
    supports_list_head[0] = recs
    recs = Supports.objects.filter( ptype = 1 ).order_by( '-id' )[:5]
    supports_list_head[1] = recs
    data['supports_list_head'] = supports_list_head

    solution_list_head = []
    sts = SolutionType.objects.all()
    for p in sts:
        t = {}
        t['type'] = p
        t['resc'] = Solution.objects.filter( ptype = p ).order_by( '-id' )[:5]
        solution_list_head.append( t )

    data['solution_list_head'] = solution_list_head
    return data
