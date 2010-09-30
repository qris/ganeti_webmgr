import urllib2
import os
import socket


from django import forms
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.http import HttpResponseRedirect, HttpResponseForbidden
from django.shortcuts import get_object_or_404, render_to_response


from ganeti_webmgr.ganeti.models import *
from ganeti_webmgr.util.portforwarder import forward_port

def detail(request, cluster_slug):
    cluster = get_object_or_404(Cluster, slug=cluster_slug)
    return render_to_response("cluster.html", {
        'cluster': cluster
    })

def list(request):        
    cluster_list = Cluster.objects.all()
    return render_to_response("cluster_list.html", {'cluster_list': cluster_list })