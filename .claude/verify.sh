#!/usr/bin/env bash
set -euo pipefail

cd "$(dirname "$0")/.."

# Activate venv if it exists
if [ -d venv ]; then
    source venv/bin/activate
fi

# Quick syntax check
python3 -c "import py_compile; py_compile.compile('bot.py', doraise=True)"
python3 -c "
import py_compile
for f in __import__('glob').glob('src/*.py'):
    py_compile.compile(f, doraise=True)
"
echo '✓ verify.sh: syntax OK'

# Test tarot fetch + astrology (without webhook)
python3 -c "
from src.tarot_data import fetch_tarot_cards, pick_card_of_the_day
from src.astrology import create_subject, create_transit_subject, get_natal_summary, get_transit_aspects

cards = fetch_tarot_cards()
assert len(cards) == 78, f'Expected 78 cards, got {len(cards)}'
card = pick_card_of_the_day(cards)
assert card['name'], 'Card name empty'

nam = create_subject('Nam', 1996, 1, 1, 0, 30)
nu = create_subject('Nu', 1996, 3, 28, 10, 0)
transit = create_transit_subject()

nam_t = get_transit_aspects(nam, transit)
nu_t = get_transit_aspects(nu, transit)
assert isinstance(nam_t, str) and len(nam_t) > 0
assert isinstance(nu_t, str) and len(nu_t) > 0

print('✓ verify.sh: integration OK')
"
echo '✓ All checks passed'
