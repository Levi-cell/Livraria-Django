DEPENDÊNCIAS:

1 - pip install django

2 - pip install gunicorn

3 - pip install whitenoise

4 - pip install djangorestframework

5 - pip install flake8

6 - pip install black

7 - pip install djangorestframework-simplejwt

8 - pip install drf-spectacular

9 - pip install django-cors-headers

Observação: após instar a quarta dependência, vá no arquivo settings do seu projeto e em installed_apps acrescente rest_farmework

COMANDOS:

1 - django-admin startproject Livraria

2 - python manage.py runserver

3 - python manage.py migrate

4 - python manage.py createsuperuser

5 - python manage.py startapp core

DEPLOY DO PROJETO:

1 - Em settings do projeto, insira na variável middleware a seguinte linha de comando: "whitenoise.middleware.WhiteNoiseMiddleware",

2 - No final do arquvio settings insira a linha de comando: STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

3 - Faça o seguinte comando no terminal: python manage.py collectstatic --noinput

INTEGRAÇÃO GIT E HEROKU:

1 - crie um repositorio no GitHub

2 - suba o projeto para esse repositório

3 - crie um arquivo gitignore o conteúdo do arquivo você irá gerar no site do gitignore, use Django e Pycharm. use o site gitignore.io

4 - No gitignore comente a parte de banco de dados do sqlite, geralmente fica na linha 10 e 11.

NOTAS IMPORTANTES:

1 - Caso queira acessar a documentação desse projeto acesse este Link: https://docs.google.com/document/d/1Tc_PpOei8wdtpJLZ6h2Sa4pa72p8WtEZN4q8g2d-dB4/edit

2 - Você também pode acessa a pasta Content nela contém uma imagem com todas as rotas disponíveis 

3 - A rota para você ter acesso a todas as classes e métodos é: http://localhost:8000/api/swagger/#/api/api_compras_partial_update

4 - A rota default é: http://localhost:8000/

