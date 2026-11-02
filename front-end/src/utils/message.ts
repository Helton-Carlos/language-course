export const MESSAGES = {
  error: {
    network: 'Não foi possível conectar ao servidor.',
    unexpected: 'Erro inesperado. Tente novamente.',
    invalidData: 'Verifique os dados informados.',
    invalidValue: 'Valor inválido',
    languagesLoad: 'Não foi possível carregar os idiomas.',
    placementLoad: 'Não foi possível carregar o teste.',
    podcastsLoad: 'Não foi possível carregar os podcasts.',
    phrasesLoad: 'Não foi possível carregar as frases.',
    request: (status: number, method: string, path: string) =>
      `Erro ${status} em ${method} ${path}`,
  },

  validation: {
    nameRequired: 'Informe seu nome.',
    emailRequired: 'Informe seu e-mail.',
    passwordMin: (min: number) => `A senha deve ter pelo menos ${min} caracteres.`,
    passwordMismatch: 'As senhas não conferem.',
  },

  success: {
    login: 'Login realizado com sucesso.',
    register: 'Conta criada com sucesso. Faça login para continuar.',
    profile: 'Idioma e nível salvos.',
    logout: 'Você saiu da conta.',
    accountDeleted: 'Sua conta foi cancelada.',
  },

  pending: {
    login: 'Entrando...',
    register: 'Criando sua conta...',
    profile: 'Salvando idioma e nível...',
    languagesLoad: 'Carregando idiomas...',
    placementLoad: 'Carregando perguntas...',
    accountDelete: 'Cancelando conta...',
    podcastsLoad: 'Carregando podcasts...',
    phrasesLoad: 'Carregando frases...',
  },

  reminder: {
    useRegisteredCredentials: 'Use o e-mail e a senha cadastrados para entrar.',
  },
} as const;
