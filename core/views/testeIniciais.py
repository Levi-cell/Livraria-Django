from django.http import HttpResponse

def teste2(request):
    return HttpResponse(
        "Essa é a rota de guia padrão, você pode acessar as seguintes rotas:  \n"
        'admin/...'
        'api/schema/...'
        'api/swagger/...'
        'api/redoc/...'
        'token/...'
        'token/refresh/...'
        'guia/...'
        'categorias-class/...'
        'categorias-class/<int:id>/...'
        'categorias-apiview/...'
        'categorias-apiview/<int:id>/...'
        'categorias-generic/...'
        'categorias-generic/<int:id>/...'
        'api/categorias...'
        'api/editoras...'
        'api/autores...'
        'api/livros...'
        'api/compras...')
