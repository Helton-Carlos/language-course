import pluginVue from 'eslint-plugin-vue';
import tseslint from 'typescript-eslint';
import vueParser from 'vue-eslint-parser';

const ALLOWED_DIRECTIVES = /^\s*(eslint-|@ts-)/;

const noComments = {
  meta: {
    type: 'problem',
    schema: [],
    messages: {
      noComments: 'Comentários não são permitidos neste projeto.',
    },
  },
  create(context) {
    const { sourceCode } = context;

    function report(comment) {
      if (ALLOWED_DIRECTIVES.test(comment.value)) {
        return;
      }
      context.report({ loc: comment.loc, messageId: 'noComments' });
    }

    return {
      Program() {
        sourceCode.getAllComments().forEach(report);
        sourceCode.ast.templateBody?.comments?.forEach(report);
      },
    };
  },
};

export default [
  {
    ignores: ['dist/**', 'node_modules/**', '.venv/**'],
  },
  {
    files: ['**/*.{js,mjs,ts,vue}'],
    languageOptions: {
      parser: vueParser,
      parserOptions: {
        parser: tseslint.parser,
        ecmaVersion: 'latest',
        sourceType: 'module',
        extraFileExtensions: ['.vue'],
      },
    },
    plugins: {
      local: { rules: { 'no-comments': noComments } },
    },
    rules: {
      'local/no-comments': 'error',
      'no-multiple-empty-lines': ['error', { max: 1, maxBOF: 0, maxEOF: 0 }],
    },
  },
  {
    files: ['**/*.vue'],
    plugins: {
      vue: pluginVue,
    },
    rules: {
      'vue/attributes-order': [
        'error',
        {
          alphabetical: false,
          order: [
            'DEFINITION',
            'LIST_RENDERING',
            'CONDITIONALS',
            'RENDER_MODIFIERS',
            'GLOBAL',
            ['UNIQUE', 'SLOT'],
            'TWO_WAY_BINDING',
            'OTHER_DIRECTIVES',
            'OTHER_ATTR',
            'EVENTS',
            'CONTENT',
          ],
        },
      ],
      'vue/max-attributes-per-line': [
        'error',
        { singleline: { max: 3 }, multiline: { max: 1 } },
      ],
      'vue/first-attribute-linebreak': [
        'error',
        { singleline: 'ignore', multiline: 'below' },
      ],
      'vue/html-closing-bracket-newline': [
        'error',
        { singleline: 'never', multiline: 'always' },
      ],
      'vue/html-indent': ['error', 2],
    },
  },
];
