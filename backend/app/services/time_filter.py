def filter_quick_recipes(recipes: list[dict], max_minutes: int = 30):
    return [
        r for r in recipes
        if r.get("time_minutes", 999) <= max_minutes
    ]
