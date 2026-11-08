READING_BANDS = ("A1-A2", "B1-B2", "C1-C2")

READING_THEMES = [
    {"key": "viagens", "label": "Viagens", "description": "Aeroporto, hotel, direções e ingressos."},
    {"key": "tecnologia", "label": "Tecnologia", "description": "Celulares, computadores, aplicativos e entrevistas."},
    {"key": "gastronomia", "label": "Gastronomia", "description": "Restaurantes, reservas, mercado e receitas."},
    {"key": "noticias", "label": "Notícias", "description": "Manchetes, economia, clima e esportes."},
]

READING_SITUATIONS = {
    "viagens": [
        {"key": "aeroporto", "title": "No aeroporto", "description": "Check-in e embarque."},
        {"key": "hotel", "title": "No hotel", "description": "Chegada, quarto e problemas."},
        {"key": "direcoes", "title": "Pedindo direções", "description": "Encontrar o caminho numa cidade nova."},
        {"key": "ingressos", "title": "Comprando ingressos", "description": "Cinema, shows e eventos."},
    ],
    "tecnologia": [
        {"key": "celular", "title": "Celular novo", "description": "Configurar e migrar um aparelho."},
        {"key": "computador", "title": "Problemas no computador", "description": "Relatar e resolver falhas."},
        {"key": "aplicativo", "title": "Escolhendo um aplicativo", "description": "Permissões e avaliações."},
        {"key": "entrevista", "title": "Entrevista de emprego", "description": "Falar sobre experiência e projetos."},
    ],
    "gastronomia": [
        {"key": "restaurante", "title": "No restaurante", "description": "Pedir e reclamar com educação."},
        {"key": "reserva", "title": "Fazendo uma reserva", "description": "Marcar, alterar e confirmar mesas."},
        {"key": "mercado", "title": "No mercado", "description": "Comprar ingredientes e economizar."},
        {"key": "receita", "title": "Seguindo uma receita", "description": "Cozinhar passo a passo."},
    ],
    "noticias": [
        {"key": "manchete", "title": "Lendo manchetes", "description": "Entender o título e o conteúdo."},
        {"key": "economia", "title": "Economia", "description": "Preços, juros e orçamento."},
        {"key": "clima", "title": "Clima", "description": "Previsões e alertas."},
        {"key": "esportes", "title": "Esportes", "description": "Resultados e análises de partidas."},
    ],
}


def band_for_level(level: str | None) -> str:
    if level in ("C1", "C2"):
        return "C1-C2"
    if level in ("B1", "B2"):
        return "B1-B2"
    return "A1-A2"
