from datetime import datetime
from kerykeion import AstrologicalSubjectFactory, AspectsFactory

from . import interpretations as interp

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


def get_natal_interpretation(subject):
    points = {
        "Sun": subject.sun, "Moon": subject.moon,
        "Mercury": subject.mercury, "Venus": subject.venus, "Mars": subject.mars,
    }
    lines = []
    for name, p in points.items():
        sign_mark = _sign_symbol(p.sign)
        retro = " ℞" if getattr(p, 'retrograde', False) else ""
        lines.append(f"**{interp.PLANET_VI.get(name, name)}** ♆ {interp.sign_vn(p.sign)} {sign_mark} {p.position:.1f}°{retro} — {interp.house_vn(p.house)}")
        expl = interp.interpret_natal_planet(name, p.sign[:3], p.house)
        if expl:
            lines.append(f"> {expl}")

    asc_str = f"**Mọc** ♆ {interp.sign_vn(subject.first_house.sign)} {_sign_symbol(subject.first_house.sign)} {subject.first_house.position:.1f}°"
    mc_str = f"**MC** ♆ {interp.sign_vn(subject.medium_coeli.sign)} {_sign_symbol(subject.medium_coeli.sign)} {subject.medium_coeli.position:.1f}°"

    overview = interp.summarize_star_sign(subject.sun.sign[:3], subject.first_house.sign[:3])

    return {
        "positions": "\n".join(lines),
        "asc_mc": f"{asc_str} · {mc_str}",
        "overview": overview,
    }


def get_transit_interpretation(natal_subject, transit_subject):
    aspects = AspectsFactory.dual_chart_aspects(
        natal_subject, transit_subject,
        first_subject_is_fixed=True,
        active_points=PERSONAL_PLANETS,
    )
    aspect_list = []
    lines = []
    for a in aspects.aspects[:8]:
        aspect_list.append({"p1": a.p1_name, "p2": a.p2_name, "aspect": a.aspect, "orbit": a.orbit})
        expl = interp.interpret_transit_aspect(a.p1_name, a.p2_name, a.aspect, a.orbit)
        lines.append(expl)

    transit_sun = transit_subject.sun
    day_sunmary = interp.summarize_day("Sun", transit_sun.sign[:3])
    outlook = interp.get_aspect_outlook(aspect_list)

    return {
        "aspects": "\n\n".join(lines),
        "day_summary": day_sunmary,
        "outlook": outlook,
    }
