# language-course

Plataforma web para estudar inglês, com leitura interativa, vocabulário pessoal e revisão por repetição espaçada.

> Projeto em desenvolvimento ativo. Funcionalidades, estrutura e documentação ainda podem mudar.

<img width="1920" height="2768" alt="pagina" src="https://github.com/user-attachments/assets/d33d0831-3adc-4318-9303-e590a0884530" />

## Funcionalidades

Depois do login, o aluno define o nível (A1 a C2), manualmente ou pelo teste de nível, e acessa:

- **Biblioteca:** textos por tema e situação, adaptados ao nível, e textos próprios importados pelo aluno.
- **Leitor interativo:** palavras clicáveis com tradução, definição, pronúncia e sugestões de significado. Também é possível selecionar uma frase de até 8 palavras.
- **Vocabulário:** lista das palavras e frases salvas, com cinco níveis de conhecimento (Novo, Reconhecido, Familiar, Aprendido e Conhecido), busca, edição e remoção.
- **Revisão:** cartões com repetição espaçada e atalhos de teclado.
- **Estatísticas:** sequência de dias, palavras conhecidas, palavras lidas e atividade dos últimos 7 dias.
- **Meta do dia:** progresso diário exibido na visão geral do dashboard.
- **Conteúdos extras:** livros por tema, podcasts em vídeo e frases e gírias com tradução.
- **PWA:** o app pode ser instalado no celular ou no computador.

Os textos e as telas estão em português. O conteúdo de estudo é somente em inglês.

## Tecnologias

| Camada | Tecnologias |
| --- | --- |
| Front-end | Vue 3, TypeScript, Vite, Vue Router, TanStack Query, Tailwind CSS 4, VueUse, Lucide, PWA |
| Back-end | Python 3.14, FastAPI, SQLAlchemy (async), Alembic, PostgreSQL, JWT em cookie, Argon2 |

## Estrutura

```
language-course/
├── back-end/    API FastAPI, models, migrations e scripts
└── front-end/   Aplicação Vue 3
```

Cada pasta tem um README com os detalhes: [back-end](back-end/README.md) e [front-end](front-end/README.md).

## Como rodar

Pré-requisitos: [uv](https://docs.astral.sh/uv/), Node.js 24 e PostgreSQL.

1. Crie o banco `language_data` no PostgreSQL.
2. Configure e inicie a API, seguindo o [README do back-end](back-end/README.md). Ela sobe em `http://localhost:8000`.
3. Configure e inicie o front-end, seguindo o [README do front-end](front-end/README.md). Ele sobe em `http://localhost:3001`.

## Licença

Projeto sem licença definida até o momento.
