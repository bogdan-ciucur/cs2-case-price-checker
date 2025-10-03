import requests
import time
import re
import random

def parse_price(price_str: str):
    """Extracts numeric value from price string like '3,50€', '€3.50', 'R$ 1,23'."""
    if not price_str:
        return None
    match = re.search(r"[\d.,]+", price_str)
    if match:
        return float(match.group(0).replace(",", "."))
    return None

def get_case_price(case_name: str):
    url = f"https://steamcommunity.com/market/priceoverview/?appid=730&currency=3&market_hash_name={case_name}"
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"Request error for {case_name}: {e}")
        return None

    try:
        data = response.json()
    except ValueError:
        print(f"Invalid JSON response for {case_name}")
        return None

    if not data.get("success"):
        print(f"No price data for {case_name}")
        return None

    price = parse_price(data.get("lowest_price", ""))
    if price is None:
        print(f"Warning: Could not parse price '{data.get('lowest_price')}' for {case_name}")
    return price

cases = {
    "Fracture Case": 40,
    "Snakebite Case": 4,
    "Clutch Case": 13,
    "Prisma Case": 5,
    "Prisma 2 Case": 5,
    "Danger Zone Case": 9,
    "Revolver Case": 1,
    "Spectrum Case": 6,
    "Spectrum 2 Case": 6,
    "Horizon Case": 1,
    "CS20 Case": 2,
    "Glove Case": 13,
    "Chroma Case": 20,
    "Chroma 2 Case": 3,
    "Chroma 3 Case": 6,
    "Gamma Case": 7,
    "Gamma 2 Case": 7,
    "Operation Breakout Weapon Case": 29,
    "Operation Phoenix Weapon Case": 16,
    "Falchion Case": 8,
    "Recoil Case": 75,
    "Dreams & Nightmares Case": 3,
    "Kilowatt Case": 5,
    "Revolution Case": 3,
}

total_value = 0

for case, amount in cases.items():
    price = get_case_price(case)
    if price is not None:
        case_total = price * amount
        total_value += case_total
        print(f"{case}: {amount} x {price:.2f}€ = {case_total:.2f}€")
    else:
        print(f"Could not fetch price for {case}")

    delay = random.uniform(1, 2)
    time.sleep(delay)

print(f"\nTotal Inventory Value: {total_value:.2f}€")
