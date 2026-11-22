# Front-end

Aplicação do language-course, feita com Vue 3, TypeScript e Vite.

## Requisitos

- Node.js 24
- API do [back-end](../back-end/README.md) rodando

## Configuração

Copie `.env.example` para `.env`:

| Variável | Descrição | Exemplo |
| --- | --- | --- |
| `VITE_API` | URL da API, com o prefixo `/api` no final | `http://localhost:8000/api` |

## Scripts

```bash
npm install
npm run dev
npm run build
npm run preview
npm run lint
```

`npm run dev` abre o app em `http://localhost:3001`. O `build` roda `vue-tsc` antes do `vite build`.

## Tecnologias

- Vue 3 com `<script setup>` e TypeScript
- Vue Router 5, com guardas de login e de perfil completo
- TanStack Query para dados do servidor e cache
- Tailwind CSS 4
- VueUse (fala, debounce, atalhos de teclado e trava de rolagem)
- Lucide (ícones)

## Estrutura

```
src/
├── components/   Componentes base (prefixo EC), cada um com seu Type.ts
├── composables/  Acesso à API, estado compartilhado e utilitários reativos
├── layouts/      Header e footer
├── plugins/      Cliente do TanStack Query
├── routes/       Rotas e guardas
├── types/        Tipos das respostas da API
├── utils/        Constantes, mensagens, datas, níveis e funções puras
└── view/         Páginas
```

## Páginas do dashboard

| Rota | Página |
| --- | --- |
| `/dashboard` | Visão geral, com meta do dia e indicadores |
| `/dashboard/nivel` e `/dashboard/nivel/teste` | Definição de nível e teste de nível |
| `/dashboard/biblioteca` | Textos importados, leituras por tema e conteúdos |
| `/dashboard/biblioteca/importar` | Importação de texto |
| `/dashboard/biblioteca/texto/:id` | Leitor de texto importado |
| `/dashboard/ler/:tema/:situacao` | Leitor de texto da biblioteca |
| `/dashboard/vocabulario` | Vocabulário salvo |
| `/dashboard/revisar` | Revisão com cartões |
| `/dashboard/estatisticas` | Estatísticas |
| `/dashboard/livros`, `/dashboard/podcast`, `/dashboard/frases` | Conteúdos extras |

As rotas com `requiresProfile` redirecionam para `/dashboard/nivel` enquanto o aluno não tiver idioma e nível definidos.

## Convenções

- Sem comentários no código.
- Todo `ref` recebe tipo explícito, como `ref<number>(0)`.
- Blocos `watch` ficam no fim do `<script setup>`.
- Formatação de datas fica em `utils/dates.ts`.
- Textos de interface ficam em `utils/message.ts` quando se repetem ou vêm de mutations.
- Mutations usam `meta.pending` e `meta.success` para exibir toasts. Erros de API aparecem em toast automaticamente.
- Confirmações destrutivas usam `toast.confirm(...)`, não `window.confirm`.
- Tamanho de texto padrão, sem `text-sm`.
- Ícones vêm do `lucide-vue-next`, sem SVG inline.

## Leitor interativo

O componente `ECReader` quebra o texto em palavras e pinta cada uma conforme o status no vocabulário. Palavras desconhecidas ficam em azul. Ao clicar em uma palavra, ou selecionar uma frase de até 8 palavras, o `ECWordPanel` mostra tradução, definição, pronúncia e o formulário para salvar. O botão "Concluir lição" marca as palavras azuis como conhecidas e registra as palavras lidas.

Na revisão, espaço mostra a resposta, a seta para a esquerda marca erro e a seta para a direita marca acerto.
