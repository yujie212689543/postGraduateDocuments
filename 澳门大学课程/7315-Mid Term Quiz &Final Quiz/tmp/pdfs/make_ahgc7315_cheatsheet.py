from __future__ import annotations

from pathlib import Path

from PIL import Image as PILImage
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas
from reportlab.platypus import (
    Flowable,
    Image,
    KeepInFrame,
    Paragraph,
    Spacer,
    Table,
    TableStyle,
)


ROOT = Path(
    "/Users/gu/Documents/Obsidian-Vaults/postGraduateDocuments/"
    "澳门大学课程/7315-Mid Term Quiz &Final Quiz"
)
ATTACH = ROOT / "附件"
OUT_DIR = ROOT / "output" / "pdf"
TMP_DIR = ROOT / "tmp" / "pdfs"
OUT_PDF = OUT_DIR / "AHGC7315_Final_A4_CheatSheet.pdf"

FONT_REG = "/System/Library/Fonts/Supplemental/Arial Unicode.ttf"
FONT_BOLD = "/System/Library/Fonts/STHeiti Medium.ttc"
FONT_LIGHT = "/System/Library/Fonts/STHeiti Light.ttc"

pdfmetrics.registerFont(TTFont("BodyCN", FONT_REG))
pdfmetrics.registerFont(TTFont("HeadCN", FONT_BOLD))
pdfmetrics.registerFont(TTFont("LightCN", FONT_LIGHT))
pdfmetrics.registerFontFamily(
    "BodyCN",
    normal="BodyCN",
    bold="HeadCN",
    italic="BodyCN",
    boldItalic="HeadCN",
)


NAVY = colors.HexColor("#17324D")
BLUE = colors.HexColor("#2C6F9E")
TEAL = colors.HexColor("#247568")
PURPLE = colors.HexColor("#6A4A8B")
ORANGE = colors.HexColor("#AF6427")
GREEN = colors.HexColor("#4D7A35")
RED = colors.HexColor("#A6403D")
INK = colors.HexColor("#1D2833")
MUTED = colors.HexColor("#566575")
LINE = colors.HexColor("#C8D1D8")
PAPER = colors.white
SOFT = colors.HexColor("#F5F8FA")
SOFT_BLUE = colors.HexColor("#EDF5FA")
SOFT_TEAL = colors.HexColor("#EEF7F4")
SOFT_PURPLE = colors.HexColor("#F5F0F8")
SOFT_ORANGE = colors.HexColor("#FAF3EC")


styles = {
    "body": ParagraphStyle(
        "body",
        fontName="BodyCN",
        fontSize=7.35,
        leading=8.7,
        textColor=INK,
        spaceAfter=0.8 * mm,
        splitLongWords=True,
    ),
    "tiny": ParagraphStyle(
        "tiny",
        fontName="BodyCN",
        fontSize=6.55,
        leading=7.55,
        textColor=INK,
        spaceAfter=0.45 * mm,
        splitLongWords=True,
    ),
    "micro": ParagraphStyle(
        "micro",
        fontName="BodyCN",
        fontSize=5.9,
        leading=6.8,
        textColor=INK,
        spaceAfter=0.2 * mm,
        splitLongWords=True,
    ),
    "sub": ParagraphStyle(
        "sub",
        fontName="HeadCN",
        fontSize=7.9,
        leading=8.9,
        textColor=NAVY,
        spaceBefore=0.8 * mm,
        spaceAfter=0.7 * mm,
    ),
    "center": ParagraphStyle(
        "center",
        fontName="BodyCN",
        fontSize=5.2,
        leading=5.9,
        alignment=TA_CENTER,
        textColor=INK,
    ),
    "cell": ParagraphStyle(
        "cell",
        fontName="BodyCN",
        fontSize=5.95,
        leading=6.65,
        textColor=INK,
    ),
    "cellhead": ParagraphStyle(
        "cellhead",
        fontName="HeadCN",
        fontSize=5.85,
        leading=6.55,
        textColor=colors.white,
    ),
}


def P(text: str, style: str = "body") -> Paragraph:
    return Paragraph(text, styles[style])


def cell(text: str, head: bool = False) -> Paragraph:
    return P(text, "cellhead" if head else "cell")


class VectorDiagram(Flowable):
    def __init__(self, width: float, height: float, draw_fn):
        super().__init__()
        self.width = width
        self.height = height
        self.draw_fn = draw_fn

    def wrap(self, _avail_width, _avail_height):
        return self.width, self.height

    def draw(self):
        self.draw_fn(self.canv, self.width, self.height)


def draw_vowel_chart(c, w, h):
    c.saveState()
    c.setStrokeColor(INK)
    c.setLineWidth(0.7)
    c.setFont("HeadCN", 5.1)
    c.setFillColor(INK)
    c.drawCentredString(w / 2, h - 5.0, "English vowel space")
    c.setLineWidth(0.8)
    top = h - 9.0
    bottom = 3.0
    left_top = 8.0
    left_bottom = 27.0
    right = w - 8.0
    c.line(left_top, top, right, top)
    c.line(right, top, right, bottom)
    c.line(left_top, top, left_bottom, bottom)
    c.line(left_bottom, bottom, right, bottom)
    c.setFont("BodyCN", 4.4)
    c.setFillColor(MUTED)
    c.drawString(2, top + 1.2, "Front")
    c.drawCentredString(w / 2, top + 1.2, "Central")
    c.drawRightString(w - 2, top + 1.2, "Back")
    points = {
        "i": (13, top - 5),
        "ɪ": (15, top - 11),
        "e": (14, top - 17),
        "ɛ": (17, top - 23),
        "æ": (20, top - 29),
        "ə": (w / 2, top - 17),
        "ʌ": (w / 2, top - 26),
        "u": (w - 13, top - 5),
        "ʊ": (w - 15, top - 11),
        "o": (w - 14, top - 17),
        "ɔ": (w - 17, top - 23),
        "ɑ": (w - 20, top - 29),
    }
    c.setFont("BodyCN", 6.2)
    for sym, (x, y) in points.items():
        c.setFillColor(RED if sym in {"u", "ʊ", "o", "ɔ"} else INK)
        c.drawCentredString(x, y, sym)
    c.setFillColor(MUTED)
    c.setFont("BodyCN", 4.0)
    c.drawString(1, 3.0, "red = rounded")
    c.restoreState()


def draw_syllable_tree(c, w, h):
    c.saveState()
    c.setStrokeColor(INK)
    c.setFillColor(INK)
    c.setLineWidth(0.6)
    c.setFont("HeadCN", 6.0)
    c.drawCentredString(w / 2, h - 5, "splints [splɪnts]")
    c.setFont("BodyCN", 5.0)
    top_left = w / 2
    top_y = h - 10
    c.drawCentredString(top_left, top_y, "σ")
    x_on = w * 0.28
    x_rime = w * 0.73
    y_mid = h - 20
    c.line(top_left, top_y - 1, x_on, y_mid + 2)
    c.line(top_left, top_y - 1, x_rime, y_mid + 2)
    c.drawCentredString(x_on, y_mid, "Onset")
    c.drawCentredString(x_rime, y_mid, "Rime")
    x_nuc = w * 0.63
    x_coda = w * 0.83
    y_low = h - 30
    c.line(x_rime, y_mid - 1, x_nuc, y_low + 2)
    c.line(x_rime, y_mid - 1, x_coda, y_low + 2)
    c.drawCentredString(x_nuc, y_low, "Nucleus")
    c.drawCentredString(x_coda, y_low, "Coda")
    c.setFont("BodyCN", 5.4)
    c.setLineWidth(0.45)
    for x in (x_on - 6, x_on, x_on + 6):
        c.line(x_on, y_low - 1.5, x, 7.5)
    c.line(x_nuc, y_low - 1.5, x_nuc, 7.5)
    for x in (x_coda - 6, x_coda, x_coda + 6):
        c.line(x_coda, y_low - 1.5, x, 7.5)
    c.drawCentredString(x_on, 2, "s p l")
    c.drawCentredString(x_nuc, 2, "ɪ")
    c.drawCentredString(x_coda, 2, "n t s")
    c.setFont("BodyCN", 4.4)
    c.setFillColor(RED)
    c.drawRightString(w - 1, 2, "nucleus required")
    c.restoreState()


def draw_ps_tree(c, w, h):
    c.saveState()
    c.setStrokeColor(INK)
    c.setFillColor(INK)
    c.setLineWidth(0.65)
    c.setFont("HeadCN", 5.9)
    root_x, root_y = w / 2, h - 5
    c.drawCentredString(root_x, root_y, "S")
    np_x, vp_x, child_y = w * 0.28, w * 0.72, h - 15
    c.line(root_x, root_y - 1, np_x, child_y + 2)
    c.line(root_x, root_y - 1, vp_x, child_y + 2)
    c.drawCentredString(np_x, child_y, "NP")
    c.drawCentredString(vp_x, child_y, "VP")
    det_x, noun_x = w * 0.15, w * 0.38
    verb_x, obj_x = w * 0.61, w * 0.83
    low_y = h - 26
    c.line(np_x, child_y - 1, det_x, low_y + 2)
    c.line(np_x, child_y - 1, noun_x, low_y + 2)
    c.line(vp_x, child_y - 1, verb_x, low_y + 2)
    c.line(vp_x, child_y - 1, obj_x, low_y + 2)
    for x, label in [
        (det_x, "Det"),
        (noun_x, "N"),
        (verb_x, "V"),
        (obj_x, "NP"),
    ]:
        c.drawCentredString(x, low_y, label)
    obj_det_x, obj_noun_x, obj_y = w * 0.78, w * 0.92, h - 34
    c.line(obj_x, low_y - 1, obj_det_x, obj_y + 2)
    c.line(obj_x, low_y - 1, obj_noun_x, obj_y + 2)
    c.drawCentredString(obj_det_x, obj_y, "Det")
    c.drawCentredString(obj_noun_x, obj_y, "N")
    c.setFont("BodyCN", 4.9)
    c.setLineWidth(0.45)
    for x in (det_x, noun_x, verb_x):
        c.line(x, low_y - 1.5, x, 7.5)
    for x in (obj_det_x, obj_noun_x):
        c.line(x, obj_y - 1.5, x, 7.5)
    c.drawCentredString(det_x, 2, "the")
    c.drawCentredString(noun_x, 2, "child")
    c.drawCentredString(verb_x, 2, "found")
    c.drawCentredString(obj_det_x, 2, "a")
    c.drawCentredString(obj_noun_x, 2, "puppy")
    c.restoreState()


def draw_xbar(c, w, h):
    c.saveState()
    c.setStrokeColor(INK)
    c.setFillColor(INK)
    c.setLineWidth(0.6)
    c.setFont("HeadCN", 5.5)
    xp_x, xp_y = w * 0.52, h - 4
    c.drawCentredString(xp_x, xp_y, "XP")
    spec_x, bar_x, y1 = w * 0.22, w * 0.73, h - 14
    c.line(xp_x, xp_y - 1, spec_x, y1 + 2)
    c.line(xp_x, xp_y - 1, bar_x, y1 + 2)
    c.drawCentredString(spec_x, y1, "Specifier")
    c.drawCentredString(bar_x, y1, "X'")
    lower_x, adj_x, y2 = w * 0.58, w * 0.88, h - 24
    c.line(bar_x, y1 - 1, lower_x, y2 + 2)
    c.line(bar_x, y1 - 1, adj_x, y2 + 2)
    c.drawCentredString(lower_x, y2, "X'")
    c.drawCentredString(adj_x, y2, "Adjunct")
    head_x, comp_x = w * 0.45, w * 0.7
    y3 = h - 34
    c.line(lower_x, y2 - 1, head_x, y3 + 2)
    c.line(lower_x, y2 - 1, comp_x, y3 + 2)
    c.drawCentredString(head_x, y3, "X = Head")
    c.drawCentredString(comp_x, y3, "Complement")
    c.setFont("BodyCN", 4.2)
    c.setFillColor(MUTED)
    c.drawString(0, 4, "core = X + Comp; optional layers = Adjunct; outer layer = Specifier")
    c.restoreState()


def crop_source_image(name: str, box: tuple[int, int, int, int], out_name: str) -> Path:
    source = ATTACH / name
    out = TMP_DIR / out_name
    with PILImage.open(source) as im:
        im.crop(box).convert("RGB").save(out, quality=95)
    return out


def small_table(data, widths, header: bool = True, zebra: bool = True):
    converted = []
    for r, row in enumerate(data):
        converted.append(
            [cell(str(value), head=header and r == 0) for value in row]
        )
    table = Table(converted, colWidths=widths, hAlign="LEFT")
    commands = [
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 1.5),
        ("RIGHTPADDING", (0, 0), (-1, -1), 1.5),
        ("TOPPADDING", (0, 0), (-1, -1), 1.1),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 1.1),
        ("GRID", (0, 0), (-1, -1), 0.25, LINE),
    ]
    if header:
        commands.append(("BACKGROUND", (0, 0), (-1, 0), NAVY))
    if zebra:
        for row in range(1 if header else 0, len(data)):
            if (row - (1 if header else 0)) % 2 == 1:
                commands.append(("BACKGROUND", (0, row), (-1, row), SOFT))
    table.setStyle(TableStyle(commands))
    return table


def draw_card(c, x, y, w, h, title, accent, story, fill=SOFT):
    c.saveState()
    c.setFillColor(fill)
    c.setStrokeColor(colors.HexColor("#D6DEE4"))
    c.setLineWidth(0.45)
    c.roundRect(x, y, w, h, 2.1 * mm, fill=1, stroke=1)
    c.setFillColor(accent)
    c.roundRect(x, y + h - 6.2 * mm, w, 6.2 * mm, 2.1 * mm, fill=1, stroke=0)
    c.setFillColor(colors.white)
    c.setFont("HeadCN", 7.7)
    c.drawString(x + 2.2 * mm, y + h - 4.25 * mm, title)
    c.restoreState()
    inner_w = w - 3.0 * mm
    inner_h = h - 7.4 * mm
    keep = KeepInFrame(
        inner_w,
        inner_h,
        story,
        mode="shrink",
        hAlign="LEFT",
        vAlign="TOP",
    )
    keep.wrapOn(c, inner_w, inner_h)
    draw_y = y + 1.2 * mm
    if keep.height < inner_h:
        draw_y += inner_h - keep.height
    keep.drawOn(c, x + 1.5 * mm, draw_y)


def make_header(c):
    page_w, page_h = A4
    c.setFillColor(NAVY)
    c.roundRect(5 * mm, page_h - 17 * mm, page_w - 10 * mm, 12 * mm, 2.4 * mm, fill=1, stroke=0)
    c.setFillColor(colors.white)
    c.setFont("HeadCN", 12.1)
    c.drawString(8 * mm, page_h - 12.8 * mm, "AHGC7315 FINAL - 一张 A4 重点小抄")
    c.setFont("BodyCN", 5.8)
    c.setFillColor(colors.HexColor("#DCE8F1"))
    c.drawRightString(
        page_w - 8 * mm,
        page_h - 12.6 * mm,
        "先认题型 -> 套规则 -> 再查例外",
    )
    c.setFillColor(BLUE)
    c.rect(5 * mm, page_h - 18.1 * mm, (page_w - 10 * mm) * 0.42, 1.1 * mm, fill=1, stroke=0)
    c.setFillColor(TEAL)
    c.rect(
        5 * mm + (page_w - 10 * mm) * 0.42,
        page_h - 18.1 * mm,
        (page_w - 10 * mm) * 0.26,
        1.1 * mm,
        fill=1,
        stroke=0,
    )
    c.setFillColor(ORANGE)
    c.rect(
        5 * mm + (page_w - 10 * mm) * 0.68,
        page_h - 18.1 * mm,
        (page_w - 10 * mm) * 0.32,
        1.1 * mm,
        fill=1,
        stroke=0,
    )


def build_story():
    wug_path = crop_source_image(
        "AHGC7315-Acquisition-P27.png",
        (1220, 230, 1840, 1020),
        "wug_crop.png",
    )
    brain_path = crop_source_image(
        "AHGC7315-Psycholing-P45.png",
        (980, 235, 1740, 1040),
        "brain_crop.png",
    )

    phonetics = [
        P(
            "<b>Vowel</b> = 气流相对通畅；<b>Consonant</b> = 声道某处有 closure / constriction。"
            "Letter / spelling 不等于 speech sound。",
            "tiny",
        ),
        P("<b>Consonant: VPM = Voicing + Place + Manner</b>", "sub"),
        P(
            "<b>Places:</b> bilabial p b m | labiodental f v | dental θ ð | "
            "alveolar t d n s z l ɹ | post-alveolar ʃ ʒ tʃ dʒ | palatal j | "
            "velar k g ŋ | glottal h / ʔ",
            "micro",
        ),
        P(
            "<b>Manners:</b> stop / fricative / affricate / nasal / liquid / glide. "
            "[ʃ] = voiceless post-alveolar fricative; [w] = labial-velar glide.",
            "micro",
        ),
        P(
            "<b>Aspiration:</b> English 清塞音在词首送气 [pʰ tʰ kʰ]；"
            "同一音节 /s/ 后不送气 [p t k]: pat vs spin。"
            "<b>中文</b>用 aspiration 区别 搭 [ta] / 他 [tʰa]。",
            "micro",
        ),
        P(
            "<b>Spelling traps:</b> think [θ] | that [ð] | ship [ʃ] | pleasure [ʒ] | "
            "chair [tʃ] | judge [dʒ] | sing [ŋ] | red [ɹ]. English /p-b/ mainly voicing; "
            "Mandarin uses aspiration.",
            "micro",
        ),
        P("Vowels: <b>height + front/back + rounding</b>", "sub"),
        Table(
            [
                [
                    VectorDiagram(43 * mm, 31 * mm, draw_vowel_chart),
                    [
                        P("<b>Rounded only:</b> /u ʊ o ɔ/", "micro"),
                        P("<b>Tense-lax:</b> i-ɪ  e-ɛ  u-ʊ  o-ɔ", "micro"),
                        P("<b>Diphthongs:</b> /aɪ aʊ ɔɪ/", "micro"),
                        P("boat 在课程图中写 /o/；boy 是 /ɔɪ/。", "micro"),
                    ],
                ]
            ],
            colWidths=[45 * mm, 42 * mm],
            style=TableStyle(
                [
                    ("VALIGN", (0, 0), (-1, -1), "TOP"),
                    ("LEFTPADDING", (0, 0), (-1, -1), 0),
                    ("RIGHTPADDING", (0, 0), (-1, -1), 1),
                    ("TOPPADDING", (0, 0), (-1, -1), 0),
                    ("BOTTOMPADDING", (0, 0), (-1, -1), 0),
                ]
            ),
        ),
    ]

    phonology = [
        P(
            "<b>Phonetics:</b> physical sounds. <b>Phonology:</b> sound patterns in a language. "
            "<b>Minimal pair</b> = different meaning; identical except one sound in the same place.",
            "tiny",
        ),
        small_table(
            [
                ["Test", "Conclusion"],
                ["minimal pair exists", "different phonemes"],
                ["no MP + complementary + phonetically similar", "allophones of one phoneme"],
                ["complementary but dissimilar", "different phonemes"],
            ],
            [55 * mm, 32 * mm],
        ),
        P("<b>/ /</b> = phoneme; <b>[ ]</b> = actual allophone. Rule: <b>/l/ -> [r] / ___ V</b>.", "micro"),
        Table(
            [
                [
                    VectorDiagram(48 * mm, 32 * mm, draw_syllable_tree),
                    [
                        P("<b>σ = Onset + Rime</b>", "micro"),
                        P("<b>Rime = Nucleus + Coda</b>", "micro"),
                        P("<b>Nucleus is required.</b> Onset/coda optional.", "micro"),
                        P("Rules: assimilation / dissimilation / insertion / deletion.", "micro"),
                    ],
                ]
            ],
            colWidths=[50 * mm, 37 * mm],
            style=TableStyle(
                [
                    ("VALIGN", (0, 0), (-1, -1), "TOP"),
                    ("LEFTPADDING", (0, 0), (-1, -1), 0),
                    ("RIGHTPADDING", (0, 0), (-1, -1), 1),
                    ("TOPPADDING", (0, 0), (-1, -1), 0),
                    ("BOTTOMPADDING", (0, 0), (-1, -1), 0),
                ]
            ),
        ),
        P(
            "<b>Plural allomorphs:</b> [z] after voiced non-sibilant; "
            "[s] after voiceless non-sibilant; [əz] after sibilant.",
            "micro",
        ),
        P(
            "<b>Examples:</b> ship/sheep is a minimal pair (/ɪ/-/i/); "
            "English [p]/[pʰ] are allophones of /p/; Korean [r]/[l] are complementary; "
            "Greek [k]/[c] are allophones of /k/, while [k]/[x] are different phonemes.",
            "micro",
        ),
    ]

    morphology = [
        P(
            "<b>Morpheme</b> = minimal unit of meaning. "
            "<b>Free</b> can stand alone; <b>bound</b> cannot. "
            "Affixes: prefix / suffix / infix / circumfix. "
            "<b>Root</b> is the base; after adding affixes it becomes a stem.",
            "tiny",
        ),
        small_table(
            [
                ["", "Inflectional", "Derivational"],
                ["Function", "grammatical", "lexical"],
                ["Word class", "no change", "may change"],
                ["Meaning", "small/no change", "meaning change"],
                ["Order", "outer layer", "inner layer"],
            ],
            [18 * mm, 32 * mm, 36 * mm],
        ),
        P(
            "<b>English 8 inflections (all suffixes):</b> "
            "3sg -s; past -ed; progressive -ing; past participle -en; "
            "plural -s; possessive -'s; comparative -er; superlative -est.",
            "micro",
        ),
        P(
            "<b>teacher</b> 的 -er = derivational；<b>taller</b> 的 -er = inflectional。"
            "Derivation 在内、inflection 在外：commit + ment + s。"
            "English compound stress: <b>GREENhouse</b>, not green HOUSE.",
            "micro",
        ),
        P(
            "<b>Analysis method:</b> find repeated content roots first, then repeated affixes; "
            "kali = house, no- = my, mo- = your, i- = his, -mes = plural. "
            "<b>Bound roots:</b> -ceive in receive / perceive.",
            "micro",
        ),
    ]

    acquisition = [
        Table(
            [
                [
                    [
                        P(
                            "<b>Innateness / UG:</b> children are born with a grammar framework; "
                            "they learn language-specific settings.",
                            "micro",
                        ),
                        P(
                            "<b>Poverty of the stimulus:</b> input has slips, false starts and errors; "
                            "parents mostly correct content, yet children generalize.",
                            "micro",
                        ),
                        P(
                            "<b>Wug test:</b> a novel wug -> wugs /wʌgz/ proves rule generalization, "
                            "not memorization; allomorph choice shows natural classes.",
                            "micro",
                        ),
                        P(
                            "<b>L2:</b> fundamental difference + L1 transfer + fossilization. "
                            "L2 critical period = tendency, exact age disputed.",
                            "micro",
                        ),
                        P(
                            "<b>Stages:</b> babbling ~6m; first word ~12m; language explosion 2;6-3;6; "
                            "most adult syntax after ~4y.",
                            "micro",
                        ),
                    ],
                    Image(str(wug_path), width=23 * mm, height=23 * mm),
                ]
            ],
            colWidths=[66 * mm, 24 * mm],
            style=TableStyle(
                [
                    ("VALIGN", (0, 0), (-1, -1), "TOP"),
                    ("LEFTPADDING", (0, 0), (-1, -1), 0),
                    ("RIGHTPADDING", (0, 0), (-1, -1), 0),
                    ("TOPPADDING", (0, 0), (-1, -1), 0),
                    ("BOTTOMPADDING", (0, 0), (-1, -1), 0),
                ]
            ),
        )
    ]

    syntax = [
        P(
            "<b>Grammatical != meaningful:</b> <i>Colorless green ideas sleep furiously</i> "
            "is grammatical but odd. Mandarin: SVO surface order + topic-comment. "
            "<b>Constituency tests:</b> stand alone / replace by pronoun / move as a unit.",
            "tiny",
        ),
        P(
            "<b>Lexical ambiguity</b> = one word has two meanings. "
            "<b>Structural ambiguity</b> = same words, two trees: "
            "<i>Sue saw the man with the telescope</i> -> PP modifies saw or man.",
            "micro",
        ),
        P(
            "<b>Rules:</b> S -> NP VP | NP -> Det N | VP -> V NP / V PP | PP -> P NP | "
            "CP -> C S. Phrases: NP / VP / PP / AdjP / AdvP. PP must start with P.",
            "micro",
        ),
        VectorDiagram(82 * mm, 39 * mm, draw_ps_tree),
        P(
            "<b>Head</b> = core; <b>Specifier</b> limits it; <b>Complement</b> completes it; "
            "<b>Adjunct</b> is optional. Delete test: meaning incomplete -> complement; "
            "sentence still complete -> adjunct.",
            "micro",
        ),
        VectorDiagram(82 * mm, 37 * mm, draw_xbar),
        small_table(
            [
                ["Structure", "Question", "Example"],
                ["the mother of J.W.", "Spec + Head + Comp", "the | mother | of J.W."],
                ["found the child", "V + complement", "found | the child"],
                ["found child in park", "core + adjunct", "core | in the park"],
            ],
            [29 * mm, 31 * mm, 29 * mm],
        ),
        P(
            "<b>Head-initial:</b> English/Mandarin: V + Comp; P + NP. "
            "<b>Head-final:</b> Japanese/Korean: Comp + V; NP + P. "
            "<b>T/aux movement:</b> Will the puppy find it? do-support: Did the puppy find it? "
            "Subject wh-word: Who found it? <b>Agreement:</b> verb agrees with subject NP, not nearest noun.",
            "micro",
        ),
    ]

    semantics = [
        P(
            "<b>Compositionality:</b> sentence meaning = word meanings + syntactic structure. "
            "<b>A entails B:</b> if A is true, B must be true. "
            "<b>Paraphrase</b> = mutual entailment; <b>contradiction</b> = A entails not-B.",
            "tiny",
        ),
        P(
            "Jack swims beautifully -> Jack swims; NOT the reverse. "
            "postpone the meeting = put off the meeting; alive/dead = contradiction.",
            "micro",
        ),
        small_table(
            [
                ["Relation", "Test / example"],
                ["synonym", "same/very similar meaning"],
                ["antonym", "opposite: complementary / gradable / relational / contranym"],
                ["homonym", "same spelling + sound; different meaning: bark"],
                ["homograph / heteronym", "same spelling; sound may differ: dove/dove"],
                ["homophone", "same sound; spelling may differ: bear/bare"],
                ["polysemy", "multiple related meanings: diamond"],
                ["hypernym / hyponym", "animal -> dog / dog -> animal"],
            ],
            [31 * mm, 57 * mm],
        ),
        P(
            "<b>Reference</b> = real-world object; <b>sense</b> = inherent meaning content. "
            "<b>Semantic features</b> are interpretable properties (+human); "
            "<b>word embeddings</b> are learned continuous vectors. "
            "<b>Anomaly</b> = semantic conflict; <b>metaphor</b> uses world knowledge; "
            "<b>idiom</b> is non-compositional.",
            "micro",
        ),
        P("<b>Thematic roles</b> = semantic relation to the event, not grammatical subject/object.", "sub"),
        small_table(
            [
                ["Role", "Meaning", "Example"],
                ["Agent", "volitional doer", "dog in dog bit stick"],
                ["Theme", "affected undergoer", "stick"],
                ["Goal / Source", "endpoint / origin", "gave John; from him"],
                ["Location", "where event occurs", "in the park"],
                ["Instrument", "means used", "the key opened door"],
                ["Experiencer", "receives sensation", "people fear snakes"],
            ],
            [25 * mm, 31 * mm, 32 * mm],
        ),
        P(
            "<b>Passive does not change roles:</b> The stick was bitten by the dog -> "
            "stick = Theme; dog = Agent.",
            "micro",
        ),
        P(
            "<b>Feature examples:</b> cat = +animate, +four-legs, +mammal, +feline. "
            "Word embedding analogy: king - queen + sister ~ brother.",
            "micro",
        ),
    ]

    psych = [
        Table(
            [
                [
                    [
                        P(
                            "<b>Priming</b> = pre-activation by a related word: "
                            "tape->glue (semantic), tape->grape (phonological), "
                            "tape->taped (morphological).",
                            "micro",
                        ),
                        P(
                            "<b>Negative priming / Stroop:</b> suppress the distractor "
                            "(word meaning) to name ink color.",
                            "micro",
                        ),
                        P(
                            "<b>Garden path:</b> temporary ambiguity -> reanalysis. "
                            "<i>The horse raced past the barn fell</i> = the horse [that was raced past the barn] fell.",
                            "micro",
                        ),
                        P(
                            "<b>Bottom-up:</b> acoustic signal -> words -> meaning. "
                            "<b>Top-down:</b> context and expectations guide perception.",
                            "micro",
                        ),
                        P(
                            "<b>Broca:</b> labored, agrammatical, missing function words/endings. "
                            "<b>Wernicke:</b> fluent, but nonsense / naming and lexical-selection problems.",
                            "micro",
                        ),
                        P(
                            "<b>L1 critical period:</b> after it, vocabulary can develop, "
                            "but full adult-like grammar is very difficult (Genie/Chelsea).",
                            "micro",
                        ),
                    ],
                    Image(str(brain_path), width=25 * mm, height=24 * mm),
                ]
            ],
            colWidths=[65 * mm, 25 * mm],
            style=TableStyle(
                [
                    ("VALIGN", (0, 0), (-1, -1), "TOP"),
                    ("LEFTPADDING", (0, 0), (-1, -1), 0),
                    ("RIGHTPADDING", (0, 0), (-1, -1), 0),
                    ("TOPPADDING", (0, 0), (-1, -1), 0),
                    ("BOTTOMPADDING", (0, 0), (-1, -1), 0),
                ]
            ),
        )
    ]

    return phonetics, phonology, morphology, acquisition, syntax, semantics, psych


def make_pdf():
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    TMP_DIR.mkdir(parents=True, exist_ok=True)
    (
        phonetics,
        phonology,
        morphology,
        acquisition,
        syntax,
        semantics,
        psych,
    ) = build_story()

    c = canvas.Canvas(str(OUT_PDF), pagesize=A4, pageCompression=1)
    c.setTitle("AHGC7315 Final Exam - One-page A4 Cheat Sheet")
    c.setAuthor("Codex")
    c.setSubject("AHGC7315 Language and Linguistics final exam revision")
    make_header(c)

    page_w, page_h = A4
    left_x = 5 * mm
    right_x = 107 * mm
    col_w = 98 * mm
    body_top = page_h - 19 * mm
    bottom = 7 * mm

    left_specs = [
        ("01 Phonetics 语音学", BLUE, SOFT_BLUE, 84 * mm, phonetics),
        ("02 Phonology 音系学", TEAL, SOFT_TEAL, 69 * mm, phonology),
        ("03 Morphology 形态学", GREEN, colors.HexColor("#F2F7EE"), 62 * mm, morphology),
        ("09 Language Acquisition 语言习得", ORANGE, SOFT_ORANGE, 39 * mm, acquisition),
    ]
    y_top = body_top
    for title, accent, fill, height, story in left_specs:
        draw_card(c, left_x, y_top - height, col_w, height, title, accent, story, fill)
        y_top -= height + 1.5 * mm

    right_specs = [
        ("07 Syntax 句法学", BLUE, SOFT_BLUE, 124 * mm, syntax),
        ("08 Semantics 语义学", PURPLE, SOFT_PURPLE, 92 * mm, semantics),
        ("10 Psycholinguistics 心理语言学", RED, colors.HexColor("#FBF0EF"), 44 * mm, psych),
    ]
    y_top = body_top
    for title, accent, fill, height, story in right_specs:
        draw_card(c, right_x, y_top - height, col_w, height, title, accent, story, fill)
        y_top -= height + 1.5 * mm

    c.setFillColor(MUTED)
    c.setFont("BodyCN", 4.3)
    c.drawString(
        left_x,
        3.3 * mm,
        "AHGC7315 final revision | source: course PPT and refreshed notes | 2026-11-19",
    )
    c.drawRightString(page_w - 5 * mm, 3.3 * mm, "A4 | 1 page | black-and-white print friendly")
    c.showPage()
    c.save()


if __name__ == "__main__":
    make_pdf()
