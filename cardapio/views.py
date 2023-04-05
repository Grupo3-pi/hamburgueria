from django.shortcuts import render
from django.http import  HttpResponse

def cardapio(request):
    return HttpResponse('Estou em cardapio')
