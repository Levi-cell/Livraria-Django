from django.http import HttpResponse
from django.views import View
from core.models import Categoria

import json


def teste(request):
    return HttpResponse("Não seja um mongol.")


def rotaPadrao(request):
    return HttpResponse(
        "Essa é a rota padrão, você pode acessar as seguintes rotas:  \n" 
        "(/admin)..."
        "(/testes)..."
        "(/categorias)..")


class CategoriaView(View):
    def get(self, request):
        data = list(Categoria.objects.values())
        formatted_data = json.dumps(data, ensure_ascii=False)
        return HttpResponse(formatted_data, content_type="application/json")



