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
    },
  },
];
