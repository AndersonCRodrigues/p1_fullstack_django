  cat > README.md <<'EOF'
# Biblioteca

Aplicação Django para gerenciamento de um acervo de livros (cadastro e listagem),
usando SQLite em desenvolvimento e suporte a PostgreSQL via variáveis de ambiente.

## Stack

- Python / Django 6.1
- SQLite (dev) ou PostgreSQL (via `DB_ENGINE=postgresql`)
- python-dotenv para configuração via `.env`

## Configuração

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
python manage.py migrate
python manage.py runserver
```

## Rotas principais

- `/acervos/` — página inicial do app
- `/acervos/livros/` — listagem de livros
- `/acervos/novo/` — cadastro de novo livro
- `/admin/` — Django admin

