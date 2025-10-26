#!/usr/bin/env bash
# Sai do script se houver algum erro
set -o errexit

# Atualiza o PDM (garante que está instalado)
pip install --upgrade pdm

# Instala as dependências do pyproject.toml
pdm install --no-self

# Coleta os arquivos estáticos do Django
pdm run python manage.py collectstatic --no-input

# Aplica as migrações do banco de dados
pdm run python manage.py migrate