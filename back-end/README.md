# Back-end

API do language-course, feita com FastAPI, SQLAlchemy assíncrono e PostgreSQL.

## Requisitos

- Python 3.14 (definido em `.python-version`)
- [uv](https://docs.astral.sh/uv/)
- PostgreSQL com um banco criado, por padrão `language_data`

## Configuração

Copie `.env.example` para `.env` e preencha os valores:

| Variável | Descrição | Padrão |
| --- | --- | --- |
| `DB_HOST` | Host do PostgreSQL | `localhost` |
| `DB_PORT` | Porta do PostgreSQL | `5432` |
| `DB_USER` | Usuário do banco | `postgres` |
| `DB_PASSWORD` | Senha do banco | obrigatória |
| `DB_NAME` | Nome do banco | `language_data` |
| `AUTH_SECRET_KEY` | Chave usada para assinar o JWT | obrigatória |

Opcionais: `AUTH_ALGORITHM` (`HS256`), `AUTH_ACCESS_TOKEN_MINUTES` (`60`), `AUTH_COOKIE_NAME` (`access_token`), `AUTH_COOKIE_SECURE` (`false`, use `true` em HTTPS) e `CORS_ORIGINS` (`http://localhost:3001,http://127.0.0.1:3001`).

Gere uma chave segura com:

```bash
python -c "import secrets; print(secrets.token_urlsafe(48))"
```

## Executando

```bash
uv sync
uv run alembic upgrade head
uv run fastapi dev src/main.py
```

A API sobe em `http://localhost:8000`. A documentação interativa fica em `/docs`. Todas as rotas usam o prefixo `/api`.

### Criar um administrador

```bash
cd src
uv run python -m scripts.create_admin --generate
```

Opções: `--name`, `--email` e `--generate`. Sem `--generate`, a senha é lida da variável `ADMIN_PASSWORD` ou pedida no terminal.

### Migrations

```bash
uv run alembic upgrade head
uv run alembic downgrade -1
uv run alembic revision -m "descricao"
```

## Qualidade de código

O projeto usa o [Ruff](https://docs.astral.sh/ruff/) para lint e formatação, configurado no pyproject.toml (linhas de até 100 caracteres e regras E, F, I, UP e B).

```bash
uv run ruff check .
uv run ruff check . --fix
uv run ruff format .
```

As migrations de dados em migrations/versions ficam fora do lint e da formatação.

## Estrutura

```
back-end/
├── migrations/    Migrations do Alembic
├── backup/        Backups pontuais de dados
└── src/
    ├── core/          Configuração, banco, segurança, exceções e regras de domínio
    ├── models/        Models SQLAlchemy
    ├── schemas/       Schemas Pydantic de entrada e saída
    ├── repositories/  Acesso ao banco
    ├── services/      Regras de negócio
    ├── routes/        Rotas FastAPI, cookies de autenticação e dependências compartilhadas
    └── scripts/       Scripts utilitários
```

As fábricas de serviços e os tipos Annotated usados nas rotas (AuthServiceDep, CurrentUserDep e semelhantes) ficam todos em outes/dependencies.py. A leitura e a gravação do cookie de login ficam em outes/cookies.py.

Fluxo de uma requisição: `routes` valida e injeta dependências, `services` aplica as regras e `repositories` conversa com o banco. Erros de negócio herdam de `AppError` (`core/exceptions.py`) e são convertidos em resposta JSON com o campo `detail`.

## Autenticação

O login grava um JWT em cookie `HttpOnly`. As rotas protegidas usam a dependência `CurrentUserDep` e recebem o usuário a partir desse cookie. O front-end precisa enviar as requisições com `credentials: 'include'`.

## Rotas

| Grupo | Rotas |
| --- | --- |
| Auth | `POST /auth/register`, `POST /auth/login`, `POST /auth/logout`, `GET /auth/me`, `DELETE /auth/account` |
| Usuários | `GET /users`, `GET /users/{id}`, `POST /users`, `PATCH /users/{id}`, `DELETE /users/{id}`, `PUT /users/me/profile` |
| Idiomas | `GET /languages` |
| Teste de nível | `GET` e `POST /languages/{language_id}/placement-test/{level}` |
| Conteúdo | `GET /languages/{language_id}/podcasts`, `GET /languages/{language_id}/phrases` |
| Leitura | `GET /reading/themes`, `GET /reading/themes/{theme}/situations`, `GET /reading/themes/{theme}/situations/{situation}` |
| Vocabulário | `GET /vocabulary`, `GET /vocabulary/map`, `GET /vocabulary/review`, `POST /vocabulary`, `POST /vocabulary/known`, `POST /vocabulary/{id}/review`, `PATCH /vocabulary/{id}`, `DELETE /vocabulary/{id}` |
| Textos do aluno | `GET /lessons`, `POST /lessons`, `GET /lessons/{id}`, `DELETE /lessons/{id}` |
| Estatísticas | `GET /stats`, `POST /stats/reading` |
| Dicionário | `GET /dictionary/lookup?term=` |

## Regras de estudo

- **Níveis de palavra:** de 1 (Novo) a 5 (Conhecido). Palavras no nível 5 não entram na revisão.
- **Repetição espaçada:** acertar sobe um nível e errar desce um. A próxima revisão ocorre em 1, 2, 4 ou 8 dias, conforme o nível. Só entram na revisão palavras com significado preenchido.
- **Meta diária:** 10 pontos por dia. Cada palavra salva e cada cartão revisado vale um ponto.
- **Sequência:** dias seguidos com qualquer atividade (palavra salva, revisão ou leitura concluída).
- **Fuso horário:** o dia da meta e da sequência usa UTC-3.
- **Dicionário:** consulta os serviços públicos MyMemory (tradução para pt-BR) e dictionaryapi.dev (definição e fonética). Se algum falhar, a resposta vem sem esses campos. Os resultados ficam em cache na memória do processo.
