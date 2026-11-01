from collections.abc import Sequence

import sqlalchemy as sa
from alembic import op
from sqlalchemy.dialects import postgresql

revision: str = "e5f7a9b1c3d5"
down_revision: str | None = "d4e6f8a0b2c4"
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None

LEVELS = ["A1", "A2", "B1", "B2", "C1", "C2"]

QUESTIONS = {
    "en-US": {
        "A1": [
            ("I ___ a student.", "am", ["is", "are", "be"]),
            ("She ___ two brothers.", "has", ["have", "haves", "is"]),
            ("What is the opposite of 'big'?", "small", ["tall", "long", "old"]),
        ],
        "A2": [
            ("Yesterday we ___ to the cinema.", "went", ["go", "goed", "gone"]),
            ("There isn't ___ milk in the fridge.", "any", ["some", "a", "many"]),
            ("My brother is ___ than me.", "taller", ["tall", "tallest", "more tall"]),
        ],
        "B1": [
            ("If it rains tomorrow, we ___ at home.", "will stay", ["staying", "would stay", "stayed"]),
            ("I have lived here ___ 2015.", "since", ["for", "from", "during"]),
            ("The book ___ by millions of people.", "has been read", ["has read", "is reading", "have read"]),
        ],
        "B2": [
            ("If I ___ more time, I would learn another language.", "had", ["have", "would have", "will have"]),
            ("He denied ___ the window.", "breaking", ["to break", "break", "to have break"]),
            ("By the time we arrived, the film ___.", "had already started", ["already started", "has already started", "was already starting"]),
        ],
        "C1": [
            ("Hardly ___ the house when it started to rain.", "had he left", ["he had left", "he left", "did he left"]),
            ("She is said ___ the best surgeon in the country.", "to be", ["being", "be", "to being"]),
            ("The manager insisted that the report ___ by Friday.", "be finished", ["is finished", "was finished", "will be finished"]),
        ],
        "C2": [
            ("Choose the word closest in meaning to 'ubiquitous'.", "omnipresent", ["rare", "ancient", "hidden"]),
            ("No sooner had she sat down ___ the phone rang.", "than", ["when", "that", "then"]),
            ("The politician's remarks were deliberately ___, leaving room for several interpretations.", "ambiguous", ["unequivocal", "explicit", "candid"]),
        ],
    },
    "es-ES": {
        "A1": [
            ("Yo ___ de Brasil.", "soy", ["eres", "es", "somos"]),
            ("¿Cómo te ___?", "llamas", ["llamo", "llama", "llaman"]),
            ("El contrario de «grande» es:", "pequeño", ["alto", "largo", "viejo"]),
        ],
        "A2": [
            ("Ayer ___ al mercado y compré frutas.", "fui", ["voy", "iré", "voy a ir"]),
            ("Mi hermano es ___ que yo.", "más alto", ["muy alto", "tan alto", "el más alto"]),
            ("Nosotros ___ en Madrid desde hace un año.", "vivimos", ["vivo", "vives", "viven"]),
        ],
        "B1": [
            ("Si mañana ___, nos quedaremos en casa.", "llueve", ["lloverá", "lloviera", "llovería"]),
            ("Cuando era niño, ___ al parque todos los días.", "iba", ["fui", "he ido", "iré"]),
            ("Cuando llegué a casa, mi hermano ya ___ la cena.", "había preparado", ["preparaba", "prepara", "preparará"]),
        ],
        "B2": [
            ("Si hubiera estudiado más, ___ el examen.", "habría aprobado", ["aprobaré", "aprobaría", "aprobé"]),
            ("Dudo que ellos ___ a tiempo.", "lleguen", ["llegan", "llegarán", "llegaron"]),
            ("Me alegro de que ___ venido.", "hayas", ["has", "habías", "hubieras"]),
        ],
        "C1": [
            ("Aunque ___ mucho dinero, no sería feliz.", "tuviera", ["tengo", "tendré", "tenía"]),
            ("Se lo dije ___ no se enterara nadie.", "para que", ["porque", "aunque", "mientras"]),
            ("Habría sido mejor que nos ___ antes.", "avisaran", ["avisaron", "avisan", "avisarán"]),
        ],
        "C2": [
            ("Elige el sinónimo de «efímero»:", "pasajero", ["duradero", "antiguo", "sólido"]),
            ("Su discurso fue tan ___ que nadie pudo contradecirlo.", "irrefutable", ["falaz", "superfluo", "insulso"]),
            ("«A buen entendedor, pocas palabras bastan» significa que:", "quien comprende rápido no necesita explicaciones largas", ["hay que hablar mucho", "las palabras son peligrosas", "entender es difícil"]),
        ],
    },
    "fr-FR": {
        "A1": [
            ("Je ___ étudiant.", "suis", ["es", "est", "êtes"]),
            ("Elle ___ deux frères.", "a", ["ai", "as", "ont"]),
            ("Le contraire de « grand » est :", "petit", ["long", "vieux", "haut"]),
        ],
        "A2": [
            ("Hier, nous ___ au cinéma.", "sommes allés", ["allons", "irons", "allions"]),
            ("Il n'y a pas ___ lait dans le frigo.", "de", ["du", "des", "le"]),
            ("Mon frère est ___ que moi.", "plus grand", ["très grand", "le plus grand", "trop grand"]),
        ],
        "B1": [
            ("S'il pleut demain, nous ___ à la maison.", "resterons", ["restons", "resterions", "sommes restés"]),
            ("Je connais Paul ___ dix ans.", "depuis", ["pendant", "il y a", "dans"]),
            ("Le livre ___ par des millions de personnes.", "a été lu", ["a lu", "est lisant", "avait lu"]),
        ],
        "B2": [
            ("Si j'avais plus de temps, j'___ une autre langue.", "apprendrais", ["apprendrai", "aurais appris", "apprenais"]),
            ("Il faut que tu ___ à l'heure.", "viennes", ["viens", "venir", "viendras"]),
            ("Quand nous sommes arrivés, le film ___ déjà commencé.", "avait", ["a", "aura", "avait eu"]),
        ],
        "C1": [
            ("Bien qu'il ___ fatigué, il a continué à travailler.", "soit", ["est", "serait", "sera"]),
            ("Le projet, ___ nous parlions hier, est approuvé.", "dont", ["que", "lequel", "où"]),
            ("Il a fait comme si de rien ___.", "n'était", ["n'est", "n'avait été", "ne serait"]),
        ],
        "C2": [
            ("Quel est le synonyme de « éphémère » ?", "passager", ["durable", "ancien", "solide"]),
            ("À peine était-elle arrivée ___ le téléphone sonna.", "que", ["et", "donc", "mais"]),
            ("« Avoir le cafard » signifie :", "être triste", ["avoir faim", "être en colère", "être malade"]),
        ],
    },
    "de-DE": {
        "A1": [
            ("Ich ___ Student.", "bin", ["bist", "ist", "sind"]),
            ("Er ___ zwei Brüder.", "hat", ["habe", "hast", "haben"]),
            ("Das Gegenteil von „groß“ ist:", "klein", ["lang", "alt", "hoch"]),
        ],
        "A2": [
            ("Gestern ___ wir ins Kino gegangen.", "sind", ["haben", "werden", "waren"]),
            ("Ich gehe ___ Schule.", "in die", ["in der", "im", "zu den"]),
            ("Mein Bruder ist ___ als ich.", "größer", ["groß", "am größten", "großer"]),
        ],
        "B1": [
            ("Wenn es morgen regnet, ___ wir zu Hause.", "bleiben", ["blieben", "geblieben", "bleibt"]),
            ("Ich wohne ___ zehn Jahren in Berlin.", "seit", ["vor", "für", "ab"]),
            ("Das Buch ___ von Millionen Menschen gelesen.", "wird", ["hat", "ist", "kann"]),
        ],
        "B2": [
            ("Wenn ich mehr Zeit ___, würde ich Spanisch lernen.", "hätte", ["habe", "hatte", "haben"]),
            ("Ich bestehe ___ einer Änderung des Vertrags.", "auf", ["für", "an", "zu"]),
            ("Das ist der Mann, ___ ich gestern gesprochen habe.", "mit dem", ["der", "dem", "mit den"]),
        ],
        "C1": [
            ("Hätte ich das gewusst, ___ ich anders entschieden.", "hätte", ["habe", "wäre", "würde"]),
            ("Er tat, als ___ er nichts gehört.", "hätte", ["hat", "haben", "hatte"]),
            ("Trotz der ___ Wetterlage fand das Fest statt.", "ungünstigen", ["ungünstige", "ungünstig", "ungünstiger"]),
        ],
        "C2": [
            ("Welches Wort bedeutet ungefähr dasselbe wie „vergänglich“?", "flüchtig", ["dauerhaft", "alt", "stabil"]),
            ("Seine Äußerungen waren bewusst ___, sodass sie unterschiedlich gedeutet werden konnten.", "mehrdeutig", ["eindeutig", "wörtlich", "unmissverständlich"]),
            ("„Das ist nicht mein Bier“ bedeutet:", "Das ist nicht meine Angelegenheit", ["Ich mag kein Bier", "Ich habe Durst", "Das ist zu teuer"]),
        ],
    },
    "zh-CN": {
        "A1": [
            ("我___学生。", "是", ["有", "在", "不"]),
            ("“你好”是什么意思？", "Olá", ["Tchau", "Obrigado", "Desculpe"]),
            ("我有两___书。", "本", ["个", "只", "张"]),
        ],
        "A2": [
            ("这是我的书，那是___书。", "他的", ["他", "是他", "他是"]),
            ("你住___哪儿？", "在", ["是", "有", "去"]),
            ("我___喝咖啡，我喝茶。", "不", ["没", "别", "非"]),
        ],
        "B1": [
            ("如果明天下雨，我们就___在家。", "待", ["来", "去", "到"]),
            ("他汉语说得___流利。", "很", ["把", "被", "给"]),
            ("这本书___很多人读过。", "被", ["把", "让", "给"]),
        ],
        "B2": [
            ("___你不说，我也知道。", "即使", ["因为", "所以", "由于"]),
            ("他把作业___完了。", "做", ["吃", "走", "唱"]),
            ("虽然很累，___他还是坚持工作。", "但是", ["因为", "所以", "如果"]),
        ],
        "C1": [
            ("这个问题不是三言两语___说清楚的。", "能", ["可", "会", "得"]),
            ("他的演讲___人深思。", "令", ["发", "给", "向"]),
            ("与其坐在这里抱怨，___去想办法解决。", "不如", ["不但", "于是", "难道"]),
        ],
        "C2": [
            ("“画蛇添足”的意思是？", "做多余的事，反而不好", ["画得很像", "非常小心", "学习绘画"]),
            ("他的话___，让人捉摸不透。", "模棱两可", ["直截了当", "一针见血", "言简意赅"]),
            ("下列哪个词与“慷慨”意思最接近？", "大方", ["吝啬", "谨慎", "懒惰"]),
        ],
    },
    "ja-JP": {
        "A1": [
            ("わたしは がくせい___。", "です", ["ます", "を", "が"]),
            ("「ありがとう」はポルトガル語で？", "Obrigado", ["Desculpe", "Tchau", "Bom dia"]),
            ("これ___ ほんです。", "は", ["を", "に", "で"]),
        ],
        "A2": [
            ("きのう えいがを ___。", "みました", ["みます", "みて", "みたい"]),
            ("わたしは まいあさ コーヒー___ のみます。", "を", ["が", "に", "へ"]),
            ("この りんごは あの りんご___ おおきいです。", "より", ["から", "まで", "ほど"]),
        ],
        "B1": [
            ("ともだちに ほんを ___ もらいました。", "かして", ["かす", "かした", "かし"]),
            ("日本語を 勉強して ___ 三年になります。", "から", ["まで", "ので", "のに"]),
            ("この本は 多くの 人に ___。", "読まれています", ["読んでいます", "読ませています", "読みたいです"]),
        ],
        "B2": [
            ("もっと 時間が ___、ほかの 言語も 勉強したいです。", "あれば", ["あるから", "あっても", "あるので"]),
            ("彼は 疲れている ___、まだ 働いています。", "にもかかわらず", ["おかげで", "ために", "ように"]),
            ("先生に 宿題を ___ ました。", "出され", ["出させ", "出して", "出す"]),
        ],
        "C1": [
            ("彼の 説明は 分かりにくい ___ ない。", "わけでは", ["ことに", "ものを", "ために"]),
            ("試験に 合格した ___、喜んでばかりは いられない。", "とはいえ", ["というと", "ように", "ところに"]),
            ("彼は 英語 ___、フランス語も 話せる。", "ばかりか", ["どころか", "につき", "をもって"]),
        ],
        "C2": [
            ("「猫の手も借りたい」の意味は？", "とても忙しい", ["猫が好き", "手が痛い", "暇だ"]),
            ("彼の 発言は ___ で、さまざまに 解釈できる。", "あいまい", ["明確", "単純", "率直"]),
            ("「一石二鳥」に 最も 近い 意味は？", "一つの 行動で 二つの 利益を 得る", ["二人で 協力する", "石を 投げる", "鳥を 飼う"]),
        ],
    },
}

questions_table = sa.table(
    "placement_questions",
    sa.column("language_id", sa.Uuid),
    sa.column("level", sa.String),
    sa.column("prompt", sa.Text),
    sa.column("options", postgresql.ARRAY(sa.Text)),
    sa.column("correct_index", sa.SmallInteger),
)


def build_rows(language_ids: dict[str, object]) -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []

    for code, levels in QUESTIONS.items():
        language_id = language_ids.get(code)
        if language_id is None:
            continue

        for level, items in levels.items():
            for position, (prompt, correct, wrong) in enumerate(items):
                slot = (position + LEVELS.index(level)) % 4
                options = list(wrong)
                options.insert(slot, correct)
                rows.append(
                    {
                        "language_id": language_id,
                        "level": level,
                        "prompt": prompt,
                        "options": options,
                        "correct_index": slot,
                    }
                )

    return rows


def upgrade() -> None:
    connection = op.get_bind()
    language_ids = dict(connection.execute(sa.text("SELECT code, id FROM languages")).all())
    rows = build_rows(language_ids)
    if rows:
        op.bulk_insert(questions_table, rows)


def downgrade() -> None:
    prompts = [
        prompt
        for levels in QUESTIONS.values()
        for items in levels.values()
        for prompt, _, _ in items
    ]
    op.execute(questions_table.delete().where(questions_table.c.prompt.in_(prompts)))
