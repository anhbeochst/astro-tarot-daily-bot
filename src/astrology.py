from datetime import date, time, datetime
from kerykeion import AstrologicalSubjectFactory, AspectsFactory

HCMC_LAT = 10.8231
HCMC_LNG = 106.6297
TZ_STR = "Asia/Ho_Chi_Minh"

PERSONAL_PLANETS = ["Sun", "Moon", "Mercury", "Venus", "Mars"]


def _sign_symbol(sign):
    symbols = {
        "Ari": "♈", "Tau": "♉", "Gem": "♊", "Can": "♋",
        "Leo": "♌", "Vir": "♍", "Lib": "♎", "Sco": "♏",
        "Sag": "♐", "Cap": "♑", "Aqu": "♒", "Pis": "♓",
    }
    return symbols.get(sign[:3], "")


def create_subject(name, year, month, day, hour, minute):
    return AstrologicalSubjectFactory.from_birth_data(
        name, year, month, day, hour, minute,
        lng=HCMC_LNG, lat=HCMC_LAT, tz_str=TZ_STR, online=False,
    )


def create_transit_subject():
    now = datetime.now()
    return AstrologicalSubjectFactory.from_birth_data(
        "Transit Today",
        now.year, now.month, now.day, now.hour, now.minute,
        lng=HCMC_LNG, lat=HCMC_LAT, tz_str=TZ_STR, online=False,
    )


def get_natal_summary(subject):
    points = [
        ("Sun", subject.sun),
        ("Moon", subject.moon),
        ("Mercury", subject.mercury),
        ("Venus", subject.venus),
        ("Mars", subject.mars),
        ("Asc", subject.first_house),
        ("MC", subject.medium_coeli),
    ]
    lines = []
    for label, p in points:
        sign_mark = _sign_symbol(p.sign)
        retro = " ℞" if getattr(p, 'retrograde', False) else ""
        lines.append(f"• {label}: {p.sign} {sign_mark} {p.position:.1f}°{retro} (House {p.house})")
    return "\n".join(lines)


def get_transit_aspects(natal_subject, transit_subject):
    aspects = AspectsFactory.dual_chart_aspects(
        natal_subject, transit_subject,
        first_subject_is_fixed=True,
        active_points=PERSONAL_PLANETS,
    )
    rows = []
    aspect_icons = {
        "conjunction": "☌",
        "opposition": "☍",
        "trine": "△",
        "square": "□",
        "sextile": "✼",
        "quintile": "Q",
    }
    for a in aspects.aspects[:10]:
        icon = aspect_icons.get(a.aspect, a.aspect)
        rows.append(f"• Transit {a.p1_name} {icon} Natal {a.p2_name} ({a.orbit:.1f}°)")
    return "\n".join(rows) if rows else "• Không có góc chiêu chính hôm nay"
