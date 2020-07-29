from django.shortcuts import render, HttpResponse

# Create your views here.


def hello(request, nome):
    return HttpResponse('<h1>Hello {}<h1>'.format(nome))


def soma(request, numero1, numero2):
    return HttpResponse("<h2>Resultado da soma: {}</h2>".format(numero1 + numero2))


def subtracao(request, numero1, numero2):
    return HttpResponse("<h2>Resultado da subtração: {}</h2>".format(numero1 - numero2))


def multiplicacao(request, numero1, numero2):
    return HttpResponse("<h2>Resultado da multiplicação: {}</h2>".format(numero1 * numero2))
