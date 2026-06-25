import json
import requests
from datetime import datetime


def send_daily_report(webhook_url, tarot_card, nam_report, nu_report):
    today = datetime.now().strftime("%d/%m/%Y")

    tarot_emoji = "🔮"
    orientation_vn = "Xuôi" if tarot_card["orientation"] == "upright" else "Ngược"
    arcana_vn = "Major" if tarot_card.get("arcana") == "Major" else "Phụ"
    suit_info = f" ({tarot_card['suit']})" if tarot_card.get("suit") else ""

    embed_tarot = {
        "title": f"{tarot_emoji} Tarot: {tarot_card['name']}",
        "color": 0x9B59B6,
        "fields": [
            {"name": "Trạng thái", "value": f"**{orientation_vn}** · {arcana_vn}{suit_info}", "inline": True},
            {"name": "Nguyên tố", "value": tarot_card.get("element", "—"), "inline": True},
            {"name": "Chiêm tinh", "value": tarot_card.get("astrological", "—"), "inline": True},
            {"name": "Keywords", "value": ", ".join(tarot_card.get("keywords", [])), "inline": False},
            {"name": "Ý nghĩa", "value": tarot_card["meaning"][:500], "inline": False},
            {"name": "Tình yêu", "value": tarot_card.get("love", "—")[:300], "inline": True},
            {"name": "Sự nghiệp", "value": tarot_card.get("career", "—")[:300], "inline": True},
        ],
        "footer": {"text": f"Lá bài trong ngày — {today}"},
    }

    embed_nam = {
        "title": "♂️ Chiêm tinh hôm nay — Nam (01/01/1996 00:30)",
        "color": 0x3498DB,
        "fields": [
            {"name": "Bản đồ sao (Natal)", "value": nam_report["natal"], "inline": False},
            {"name": "Transit ảnh hưởng", "value": nam_report["transit"], "inline": False},
        ],
        "footer": {"text": f"Cập nhật {today}"},
    }

    embed_nu = {
        "title": "♀️ Chiêm tinh hôm nay — Nữ (28/03/1996 10:00)",
        "color": 0xE91E63,
        "fields": [
            {"name": "Bản đồ sao (Natal)", "value": nu_report["natal"], "inline": False},
            {"name": "Transit ảnh hưởng", "value": nu_report["transit"], "inline": False},
        ],
        "footer": {"text": f"Cập nhật {today}"},
    }

    payload = {
        "embeds": [embed_tarot, embed_nam, embed_nu],
    }

    resp = requests.post(webhook_url, json=payload, timeout=15)
    resp.raise_for_status()
    return True
