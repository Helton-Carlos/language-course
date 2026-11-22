export const MESSAGES = {
  error: {
    network: 'Não foi possível conectar ao servidor.',
    unexpected: 'Erro inesperado. Tente novamente.',
    invalidData: 'Verifique os dados informados.',
    invalidValue: 'Valor inválido',
    languagesLoad: 'Não foi possível carregar os idiomas.',
    placementLoad: 'Não foi possível carregar o teste.',
    readingLoad: 'Não foi possível carregar os textos.',
    podcastsLoad: 'Não foi possível carregar os podcasts.',
    phrasesLoad: 'Não foi possível carregar as frases.',
    vocabularyLoad: 'Não foi possível carregar seu vocabulário.',
    lessonsLoad: 'Não foi possível carregar seus textos.',
    lessonLoad: 'Não foi possível carregar o texto.',
    statsLoad: 'Não foi possível carregar suas estatísticas.',
    reviewLoad: 'Não foi possível carregar a revisão.',
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
    wordSaved: 'Palavra salva no vocabulário.',
    wordDeleted: 'Palavra removida do vocabulário.',
    lessonSaved: 'Texto adicionado à sua biblioteca.',
    lessonDeleted: 'Texto removido.',
    lessonCompleted: 'Lição concluída. As palavras azuis foram marcadas como conhecidas.',
  },

  pending: {
    login: 'Entrando...',
    register: 'Criando sua conta...',
    profile: 'Salvando idioma e nível...',
    languagesLoad: 'Carregando idiomas...',
    placementLoad: 'Carregando perguntas...',
    readingLoad: 'Carregando textos...',
    accountDelete: 'Cancelando conta...',
    podcastsLoad: 'Carregando podcasts...',
    phrasesLoad: 'Carregando frases...',
    vocabularyLoad: 'Carregando vocabulário...',
    lessonsLoad: 'Carregando textos...',
    lessonLoad: 'Carregando texto...',
    statsLoad: 'Carregando estatísticas...',
    reviewLoad: 'Carregando revisão...',
    lessonSave: 'Salvando texto...',
  },

  reminder: {
    useRegisteredCredentials: 'Use o e-mail e a senha cadastrados para entrar.',
  },
} as const;
