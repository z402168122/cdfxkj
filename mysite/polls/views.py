


from django.shortcuts import render_to_response
from django.contrib import auth
from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.template import RequestContext

def home( request, path = '', template_name = "index.html" ):

    return render_to_response( template_name, locals(), context_instance = RequestContext( request ) )




def product_list( request, product_type = 0, template_name = "list.html" ):
    return render_to_response( template_name, locals(), context_instance = RequestContext( request ) )


def product_detail( request, product_type = 0, product_id = 0, template_name = "product_dateil.html" ):
    return render_to_response( template_name, locals(), context_instance = RequestContext( request ) )


