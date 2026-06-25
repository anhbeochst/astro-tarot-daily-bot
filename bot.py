import os
import sys
import traceback

sys.path.insert(0, os.path.dirname(__file__))

from src.tarot_data import fetch_tarot_cards, pick_card_of_the_day
from src.astrology import (
    create_subject, create_transit_subject,
    get_natal_summary, get_transit_aspects,
)
from src.discord_embed import send_daily_report


def main():
    webhook_url = os.environ.get("DISCORD_WEBHOOK_URL")
    if not webhook_url:
        print("ERROR: DISCORD_WEBHOOK_URL not set")
        sys.exit(1)

    print("[1/4] Fetching tarot data...")
    cards = fetch_tarot_cards()
    card = pick_card_of_the_day(cards)
    print(f"  → Tarot: {card['name']} ({card['orientation']})")

    print("[2/4] Calculating natal charts...")
    nam = create_subject("Nam", 1996, 1, 1, 0, 30)
    nu = create_subject("Nu", 1996, 3, 28, 10, 0)
    print("  → Natal charts done")

    print("[3/4] Calculating today's transits...")
    transit = create_transit_subject()
    nam_natal = get_natal_summary(nam)
    nu_natal = get_natal_summary(nu)
    nam_transit = get_transit_aspects(nam, transit)
    nu_transit = get_transit_aspects(nu, transit)
    print("  → Transits done")

    print("[4/4] Sending Discord report...")
    send_daily_report(
        webhook_url,
        card,
        {"natal": nam_natal, "transit": nam_transit},
        {"natal": nu_natal, "transit": nu_transit},
    )
    print("  ✓ Report sent successfully!")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"ERROR: {e}")
        traceback.print_exc()
        sys.exit(1)
