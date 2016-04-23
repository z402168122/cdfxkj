


from django.shortcuts import render_to_response
from django.contrib import auth
from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.template import RequestContext

def home( request, template_name = "index.html" ):
    template_name = "index.html"
    return render_to_response( template_name, locals(), context_instance = RequestContext( request ) )
