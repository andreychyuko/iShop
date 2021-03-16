from django.shortcuts import render
from django.http import HttpResponseRedirect, Http404, HttpResponse, JsonResponse



def hello(request, name):
    return HttpResponse(f'Hello {name}')
