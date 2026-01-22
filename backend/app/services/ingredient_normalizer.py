NORMALIZATION_MAP = {
    "cherry tomatoes": "tomato",
    "tomatoes": "tomato",
    "red onion": "onion",
    "white onion": "onion",
    "spring onions": "onion",
    "bell pepper": "capsicum",
    "capsicums": "capsicum",
    "cheddar cheese": "cheese",
    "mozzarella": "cheese",
    "eggs": "egg"
}


def normalize_ingredients(ingredients: list[str]) -> list[str]:
    normalized = set()

    for item in ingredients:
        key = item.lower().strip()
        normalized.add(NORMALIZATION_MAP.get(key, key))

    return sorted(normalized)
