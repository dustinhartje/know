from django.http import HttpResponse, Http404

from django.shortcuts import get_object_or_404, render_to_response

from know.models import Server, ApplicationRole, Application, VirtualizationHost, LoadBalancer, KnowledgeItem

def index(request):
    #return HttpResponse("<h1>Hello World!</h1>")
    return render_to_response('index.html')

def servers(request):
    servers=Server.objects.all()
    return render_to_response('servers.html', {'servers': servers})

def server_detail(request, server_id):
    server = get_object_or_404(Server, pk=server_id)
    return render_to_response('server_detail.html', {'server': server})

