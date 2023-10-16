from django.http import HttpResponse, JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
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


@method_decorator(csrf_exempt, name="dispatch")
class CategoriaView(View):
    def get(self, request, id=None):
        if id:
            qs = Categoria.objects.get(id=id)
            data = {'id': qs.id, 'descricao': qs.descricao}
            return JsonResponse(data)
        else:
            data = list(Categoria.objects.values())
            formatted_data = json.dumps(data, ensure_ascii=False)
            return HttpResponse(formatted_data, content_type="application/json")

    def post(self, request):
        json_data = json.loads(request.body)
        nova_categoria = Categoria.objects.create(**json_data)
        data = {"id": nova_categoria.id, "descricao": nova_categoria.descricao}
        return JsonResponse(data)
