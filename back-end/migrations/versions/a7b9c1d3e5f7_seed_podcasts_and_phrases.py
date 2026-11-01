from collections.abc import Sequence

import sqlalchemy as sa
from alembic import op

revision: str = "a7b9c1d3e5f7"
down_revision: str | None = "f6a8b0c2d4e6"
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None

PODCASTS = {
    "en-US": [
        ("Yxnvq6dxXXw", "How to make polite conversation in this English class with Georgie"),
        ("npka43vhwNo", "Is aircon the answer to a heating world? 6 Minute English"),
        ("VFA53-P4yPo", "Tips for feeling confident in job interviews | Improve your listening with Real Easy English"),
    ],
    "es-ES": [
        ("lV8UXPvpsc0", "Intermediate Spanish Podcast about Generational Language"),
        ("aBsLpWaG4MA", "How Do You Describe Your Family? (Intermediate Spanish listening)"),
        ("_BY4j-QCbdU", "How Do Spanish Speakers Really Introduce Themselves?"),
    ],
    "fr-FR": [
        ("695ludBa7sc", "9 Beginner Questions to Get to Know Someone in French: Real Answers from the Streets."),
        ("og9R-J6bduk", "The French Describe Their Best Friend (B1 Listening Comprehension)"),
        ("0R7rt5YKbdE", "What Makes The French Angry? (B2 Listening Comprehension)"),
    ],
    "de-DE": [
        ("sd9420Fy1Qs", "Bist du nostalgisch?"),
        ("nR41ZGNuGMg", "Schöne Erlebnisse mit Freunden"),
        ("tVdNn_hlvgo", "Nerven dich Fehler?"),
    ],
    "zh-CN": [
        ("fXGNkkC7tgk", "Sentence Making with 'I like...' | Easy Mandarin 125"),
        ("UqPJ6575ff0", "Hiking in Taiwan | Easy Mandarin 127"),
        ("rGdnm7XTpVA", "Things You Must Know Before Learning Chinese | Easy Mandarin 126"),
    ],
    "ja-JP": [
        ("wy0g1qESAug", "#949 秋にやりたいこと / EASY JAPANESE PODCAST"),
        ("nwzkmQ-H2ss", "#948 着物を着てみた / EASY JAPANESE PODCAST"),
        ("xxGc0z2r1h4", "#947 届ける・報告する / EASY JAPANESE PODCAST"),
    ],
}

PHRASES = {
    "en-US": {
        "phrase": [
            ("How are you doing today?", "Como você está hoje?"),
            ("Could you help me, please?", "Você poderia me ajudar, por favor?"),
            ("I'm looking forward to it.", "Estou ansioso por isso."),
            ("It's nice to meet you.", "Prazer em conhecer você."),
            ("Can you say that again, please?", "Pode repetir, por favor?"),
        ],
        "slang": [
            ("No worries!", "Sem problemas! / Tranquilo!"),
            ("I'm swamped.", "Estou atolado de trabalho."),
            ("Wanna hang out tonight?", "Quer sair comigo hoje à noite?"),
            ("It's a piece of cake.", "É moleza."),
            ("That's awesome!", "Isso é demais!"),
        ],
    },
    "es-ES": {
        "phrase": [
            ("¿Cómo estás hoy?", "Como você está hoje?"),
            ("¿Podrías ayudarme, por favor?", "Você poderia me ajudar, por favor?"),
            ("Mucho gusto en conocerte.", "Prazer em te conhecer."),
            ("¿Puedes repetir, por favor?", "Pode repetir, por favor?"),
            ("No entiendo, ¿puedes hablar más despacio?", "Não entendo, pode falar mais devagar?"),
        ],
        "slang": [
            ("¡Qué guay!", "Que legal!"),
            ("Estoy hecho polvo.", "Estou destruído, exausto."),
            ("¡Vale!", "Beleza! / Combinado! (Espanha)"),
            ("Es pan comido.", "É moleza."),
            ("¿Qué onda?", "E aí? / Que tal? (México)"),
        ],
    },
    "fr-FR": {
        "phrase": [
            ("Comment allez-vous ?", "Como você está? (formal)"),
            ("Pouvez-vous m'aider, s'il vous plaît ?", "Você poderia me ajudar, por favor?"),
            ("Enchanté de faire votre connaissance.", "Prazer em conhecê-lo(a)."),
            ("Pouvez-vous répéter, s'il vous plaît ?", "Pode repetir, por favor?"),
            ("Je ne comprends pas.", "Eu não entendo."),
        ],
        "slang": [
            ("C'est trop bien !", "É muito legal!"),
            ("Ça roule ?", "Tudo bem? / Tudo certo?"),
            ("J'ai la flemme.", "Estou com preguiça."),
            ("Je suis crevé.", "Estou morto de cansaço."),
            ("Ça marche !", "Combinado! / Fechado!"),
        ],
    },
    "de-DE": {
        "phrase": [
            ("Wie geht es Ihnen?", "Como você está? (formal)"),
            ("Können Sie mir bitte helfen?", "Você poderia me ajudar, por favor?"),
            ("Freut mich, Sie kennenzulernen.", "Prazer em conhecê-lo(a)."),
            ("Können Sie das bitte wiederholen?", "Pode repetir, por favor?"),
            ("Ich verstehe das nicht.", "Eu não entendo isso."),
        ],
        "slang": [
            ("Alles klar!", "Tudo certo!"),
            ("Das ist mir wurscht.", "Tanto faz para mim."),
            ("Ich habe keinen Bock.", "Não estou a fim."),
            ("Krass!", "Nossa! / Que absurdo!"),
            ("Das ist ein Klacks.", "É moleza."),
        ],
    },
    "zh-CN": {
        "phrase": [
            ("你今天好吗？ (Nǐ jīntiān hǎo ma?)", "Como você está hoje?"),
            ("你能帮我吗？ (Nǐ néng bāng wǒ ma?)", "Você pode me ajudar?"),
            ("很高兴认识你。 (Hěn gāoxìng rènshi nǐ.)", "Muito prazer em te conhecer."),
            ("请再说一遍。 (Qǐng zài shuō yí biàn.)", "Por favor, repita mais uma vez."),
            ("我不明白。 (Wǒ bù míngbai.)", "Eu não entendo."),
        ],
        "slang": [
            ("太棒了！ (Tài bàng le!)", "Excelente! / Demais!"),
            ("没问题！ (Méi wèntí!)", "Sem problema!"),
            ("加油！ (Jiāyóu!)", "Força! / Vai com tudo!"),
            ("我服了。 (Wǒ fú le.)", "Eu me rendo. / Fiquei sem palavras."),
            ("小菜一碟。 (Xiǎo cài yì dié.)", "É moleza."),
        ],
    },
    "ja-JP": {
        "phrase": [
            ("お元気ですか？ (Ogenki desu ka?)", "Como você está?"),
            ("手伝っていただけますか？ (Tetsudatte itadakemasu ka?)", "Você poderia me ajudar?"),
            ("はじめまして。よろしくお願いします。 (Hajimemashite. Yoroshiku onegaishimasu.)", "Prazer em conhecê-lo(a). Conto com você."),
            ("もう一度言ってください。 (Mō ichido itte kudasai.)", "Por favor, diga mais uma vez."),
            ("分かりません。 (Wakarimasen.)", "Eu não entendo."),
        ],
        "slang": [
            ("やばい！ (Yabai!)", "Nossa! (pode ser muito bom ou muito ruim)"),
            ("めっちゃ美味しい！ (Meccha oishii!)", "Muito gostoso!"),
            ("マジで？ (Maji de?)", "Sério mesmo?"),
            ("お疲れ様！ (Otsukaresama!)", "Bom trabalho! / Obrigado pelo esforço!"),
            ("ドンマイ！ (Donmai!)", "Não se preocupe!"),
        ],
    },
}

podcasts_table = sa.table(
    "podcast_episodes",
    sa.column("language_id", sa.Uuid),
    sa.column("title", sa.String),
    sa.column("youtube_id", sa.String),
    sa.column("position", sa.SmallInteger),
)

phrases_table = sa.table(
    "phrases",
    sa.column("language_id", sa.Uuid),
    sa.column("kind", sa.String),
    sa.column("text", sa.String),
    sa.column("translation", sa.String),
    sa.column("position", sa.SmallInteger),
)


def upgrade() -> None:
    connection = op.get_bind()
    language_ids = dict(connection.execute(sa.text("SELECT code, id FROM languages")).all())

    podcast_rows = [
        {"language_id": language_ids[code], "title": title, "youtube_id": youtube_id, "position": position}
        for code, episodes in PODCASTS.items()
        if code in language_ids
        for position, (youtube_id, title) in enumerate(episodes)
    ]
    if podcast_rows:
        op.bulk_insert(podcasts_table, podcast_rows)

    phrase_rows = [
        {
            "language_id": language_ids[code],
            "kind": kind,
            "text": text,
            "translation": translation,
            "position": position,
        }
        for code, groups in PHRASES.items()
        if code in language_ids
        for kind, items in groups.items()
        for position, (text, translation) in enumerate(items)
    ]
    if phrase_rows:
        op.bulk_insert(phrases_table, phrase_rows)


def downgrade() -> None:
    youtube_ids = [youtube_id for episodes in PODCASTS.values() for youtube_id, _ in episodes]
    op.execute(podcasts_table.delete().where(podcasts_table.c.youtube_id.in_(youtube_ids)))

    texts = [text for groups in PHRASES.values() for items in groups.values() for text, _ in items]
    op.execute(phrases_table.delete().where(phrases_table.c.text.in_(texts)))
