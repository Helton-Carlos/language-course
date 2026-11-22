import { CreditCard, Gift, LockOpen } from 'lucide-vue-next';

export const FREE_BENEFITS = [
  {
    key: 'sem-mensalidade',
    title: 'Sem mensalidade',
    description: 'Estude inglês sem pagar nada pelo curso.',
    icon: Gift,
  },
  {
    key: 'sem-cartao',
    title: 'Sem cartão de crédito',
    description: 'Crie sua conta só com nome, e-mail e senha.',
    icon: CreditCard,
  },
  {
    key: 'tudo-liberado',
    title: 'Tudo liberado',
    description: 'Biblioteca, vocabulário, revisão e estatísticas disponíveis para todos.',
    icon: LockOpen,
  },
] as const;