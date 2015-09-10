from django.shortcuts import render_to_response

# Create your views here.
from django.template.context import RequestContext


def home(request):
    if request.method == 'GET':
        return render_to_response("clients_home.html", request, context_instance=RequestContext(request))