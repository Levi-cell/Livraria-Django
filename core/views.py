from django.http import HttpResponse


def teste(request):
    return HttpResponse("Minha pica é grande desgraça")


def novaRota(request):
    return HttpResponse("Eu sou viadinho")
