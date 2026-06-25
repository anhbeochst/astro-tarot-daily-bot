import requests
from datetime import datetime

FIELD_VALUE_MAX = 1024


def _truncate(text, maxlen=FIELD_VALUE_MAX):
    if len(text) > maxlen:
        return text[: maxlen - 3] + "..."
    return text


def send_daily_report(webhook_url, tarot_card, nam_report, nu_report):
    today = datetime.now().strftime("%d/%m/%Y")

    orientation_vn = "Xuôi" if tarot_card["orientation"] == "upright" else "Ngược"
    arcana_vn = "Major" if tarot_card.get("arcana") == "Major" else "Phụ"
    suit_info = f" ({tarot_card['suit']})" if tarot_card.get("suit") else ""

    embed_tarot = {
        "title": f"🔮 Tarot: {tarot_card['name']}",
        "color": 0x9B59B6,
        "fields": [
            {"name": "Trạng thái", "value": f"**{orientation_vn}** · {arcana_vn}{suit_info}", "inline": True},
            {"name": "Nguyên tố", "value": tarot_card.get("element", "—"), "inline": True},
            {"name": "Chiêm tinh", "value": tarot_card.get("astrological", "—"), "inline": True},
            {"name": "Keywords", "value": _truncate(", ".join(tarot_card.get("keywords", []))), "inline": False},
            {"name": "Ý nghĩa", "value": _truncate(tarot_card["meaning"]), "inline": False},
            {"name": "Tình yêu", "value": _truncate(tarot_card.get("love", "—")), "inline": True},
            {"name": "Sự nghiệp", "value": _truncate(tarot_card.get("career", "—")), "inline": True},
        ],
        "footer": {"text": f"Lá bài trong ngày — {today}"},
    }

    embed_nam = _build_astro_embed(
        "♂️", "Nam (01/01/1996 00:30)", 0x3498DB, nam_report, today
    )
    embed_nu = _build_astro_embed(
        "♀️", "Nữ (28/03/1996 10:00)", 0xE91E63, nu_report, today
    )

    payload = {"embeds": [embed_tarot, embed_nam, embed_nu]}
    resp = requests.post(webhook_url, json=payload, timeout=15)
    resp.raise_for_status()
    return True


def _build_astro_embed(emoji, title, color, report, today):
    fields = []
    natal = report.get("natal", {})
    transit = report.get("transit", {})

    if natal.get("overview"):
        fields.append({"name": "☀️ Tổng quan", "value": _truncate(natal["overview"]), "inline": False})
    if natal.get("positions"):
        fields.append({"name": "📍 Vị trí các hành tinh", "value": _truncate(natal["positions"]), "inline": False})
    if natal.get("asc_mc"):
        fields.append({"name": "🎯 Góc quan trọng", "value": _truncate(natal["asc_mc"]), "inline": False})

    if transit.get("day_summary"):
        fields.append({"name": "🌤 Hôm nay", "value": _truncate(transit["day_summary"]), "inline": False})
    if transit.get("outlook"):
        fields.append({"name": "📊 Tổng quan góc chiếu", "value": _truncate(transit["outlook"]), "inline": False})
    if transit.get("aspects"):
        fields.append({"name": "🔄 Các góc chiếu transit → natal", "value": _truncate(transit["aspects"]), "inline": False})

    return {
        "title": f"{emoji} Chiêm tinh — {title}",
        "color": color,
        "fields": fields,
        "footer": {"text": f"Cập nhật {today}"},
    }
