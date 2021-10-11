from django.http import HttpResponse

import socket


def index(request):
    hostname = socket.gethostname()
    html_response = f'<html><body><h1>Hostname: {hostname}</h1></body></html>'
   
    return HttpResponse(html_response)