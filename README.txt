DEPENDÊNCIAS:

1 - pip install Django

2 - pip install gunicorn

3 - pip install whitenoise

COMANDOS:

1 - django-admin startproject Livraria

2 - python manage.py runserver

3 - python manage.py migrate

4 - python manage.py createsuperuser

5 - python manage.py startapp core

DEPLOY DO PROJETO:

1 - Em settings do projeto, insira na variável middleware a seguinte linha de comando:  "whitenoise.middleware.WhiteNoiseMiddleware",

2 - No final do arquvio settings insira a linha de comando: STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

3 - Faça o seguinte comando no terminal: python manage.py collectstatic --noinput

Obs: essa parte você deixa para o final

INTEGRAÇÃO GIT E HEROKU:

1 - crie um repositorio no GitHub

2 - suba o projeto para esse repositório

3 - crie um arquivo gitignore o conteúdo do arquivo você irá gerar no site do gitignore, use Django e Pycharm.

4 - No gitignore comente a parte de banco de dados do sqlite, geralmente fica na linha 10 e 11.