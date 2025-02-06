#!/bin/bash

# Nome do projeto
PROJECT_NAME="glpi_mvp"

# Criando a estrutura de pastas
mkdir -p ${PROJECT_NAME}/{app/{models,routes,templates/{auth,ticket,asset,category},static/{css,js,images},utils},migrations,tests}

# Criando arquivos principais
touch ${PROJECT_NAME}/config.py
touch ${PROJECT_NAME}/requirements.txt
touch ${PROJECT_NAME}/run.py
touch ${PROJECT_NAME}/README.md

# Criando arquivos dentro de app/
touch ${PROJECT_NAME}/app/__init__.py
touch ${PROJECT_NAME}/app/models/__init__.py
touch ${PROJECT_NAME}/app/models/user.py
touch ${PROJECT_NAME}/app/models/ticket.py
touch ${PROJECT_NAME}/app/models/asset.py
touch ${PROJECT_NAME}/app/models/category.py
touch ${PROJECT_NAME}/app/routes/__init__.py
touch ${PROJECT_NAME}/app/routes/auth.py
touch ${PROJECT_NAME}/app/routes/ticket.py
touch ${PROJECT_NAME}/app/routes/asset.py
touch ${PROJECT_NAME}/app/routes/category.py
touch ${PROJECT_NAME}/app/utils/__init__.py
touch ${PROJECT_NAME}/app/utils/auth.py
touch ${PROJECT_NAME}/app/utils/db.py

# Criando arquivos dentro de templates/
touch ${PROJECT_NAME}/app/templates/base.html
touch ${PROJECT_NAME}/app/templates/auth/login.html
touch ${PROJECT_NAME}/app/templates/auth/register.html
touch ${PROJECT_NAME}/app/templates/ticket/list.html
touch ${PROJECT_NAME}/app/templates/ticket/detail.html
touch ${PROJECT_NAME}/app/templates/ticket/create.html
touch ${PROJECT_NAME}/app/templates/asset/list.html
touch ${PROJECT_NAME}/app/templates/asset/detail.html
touch ${PROJECT_NAME}/app/templates/asset/create.html
touch ${PROJECT_NAME}/app/templates/category/list.html
touch ${PROJECT_NAME}/app/templates/category/detail.html
touch ${PROJECT_NAME}/app/templates/category/create.html

# Criando arquivos dentro de static/
touch ${PROJECT_NAME}/app/static/css/styles.css
touch ${PROJECT_NAME}/app/static/js/scripts.js

# Criando arquivos dentro de tests/
touch ${PROJECT_NAME}/tests/__init__.py
touch ${PROJECT_NAME}/tests/test_auth.py
touch ${PROJECT_NAME}/tests/test_ticket.py
touch ${PROJECT_NAME}/tests/test_asset.py
touch ${PROJECT_NAME}/tests/test_category.py

# Mensagem de conclusão
echo "Estrutura de pastas e arquivos criada com sucesso em ${PROJECT_NAME}/!"