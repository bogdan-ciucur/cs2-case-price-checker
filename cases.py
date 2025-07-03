import requests
import time

def get_case_price(case_name):
    url = f"https://steamcommunity.com/market/priceoverview/?appid=730&currency=3&market_hash_name={case_name}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if "lowest_price" in data:
            price_str = data["lowest_price"].replace("\u20ac", "").replace(",", ".")
            try:
                return float(price_str)
            except ValueError:
                print(f"Warning: Could not convert price '{price_str}' for {case_name}")
    return None

cases = {
    "Fracture Case": 36,
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
    "Recoil Case": 74,
    "Dreams & Nightmares Case": 2,
    "Kilowatt Case": 3,
}

total_value = 0

for case, amount in cases.items():
    price = get_case_price(case)
    if price:
        case_total = price * amount
        total_value += case_total
        print(f"{case}: {amount} x {price:.2f}€ = {case_total:.2f}€")
    else:
        print(f"Could not fetch price for {case}")
    time.sleep(1)  # To prevent rate-limiting

print(f"\nTotal Inventory Value: {total_value:.2f}€")


# import requests
# import time

# def get_case_price(case_name, retries=5):
#     url = f"https://steamcommunity.com/market/priceoverview/?appid=730&currency=3&market_hash_name={case_name}"
    
#     for attempt in range(retries):
#         response = requests.get(url)
#         if response.status_code == 200:
#             data = response.json()
#             if "lowest_price" in data:
#                 price_str = data["lowest_price"].replace("\u20ac", "").replace(",", ".")
#                 try:
#                     return float(price_str)
#                 except ValueError:
#                     print(f"Warning: Could not convert price '{price_str}' for {case_name}")
#                     return None
#         else:
#             print(f"Attempt {attempt+1} failed for {case_name}. Retrying...")
#             time.sleep(3)  # Wait before retrying
    
#     print(f"Failed to fetch price for {case_name} after {retries} attempts.")
#     return None

# cases = {
#     "Fracture Case": 3,
#     "Snakebite Case": 4,
#     "Clutch Case": 13,
#     "Prisma Case": 5,
#     "Prisma 2 Case": 5,
#     "Danger Zone Case": 9,
#     "Revolver Case": 1,
#     "Spectrum Case": 6,
#     "Spectrum 2 Case": 6,
#     "Horizon Case": 1,
#     "CS20 Case": 2,
#     "Glove Case": 13,
#     "Chroma Case": 20,
#     "Chroma 2 Case": 3,
#     "Chroma 3 Case": 6,
#     "Gamma Case": 7,
#     "Gamma 2 Case": 7,
#     "Operation Breakout Weapon Case": 29,
#     "Operation Phoenix Weapon Case": 16,
#     "Falchion Case": 8
# }

# total_value = 0

# for case, amount in cases.items():
#     price = get_case_price(case)
#     if price:
#         case_total = price * amount
#         total_value += case_total
#         print(f"{case}: {amount} x {price:.2f}€ = {case_total:.2f}€")
#     else:
#         print(f"Could not fetch price for {case}")
#     time.sleep(1)  # Increased sleep time to prevent rate limiting

# print(f"\nTotal Inventory Value: {total_value:.2f}€")
