from fastapi import APIRouter, UploadFile, File
from app.services.ai_service import extract_ingredients, generate_recipes
from app.services.ingredient_normalizer import normalize_ingredients
from app.services.time_filter import filter_quick_recipes

router = APIRouter()

@router.post("/analyze-fridge")
async def analyze_fridge(image: UploadFile = File(...)):
    image_bytes = await image.read()

    raw_ingredients = await extract_ingredients(image_bytes)
    normalized_ingredients = normalize_ingredients(raw_ingredients)

    recipes = await generate_recipes(normalized_ingredients)
    quick_recipes = filter_quick_recipes(recipes)

    return {
        "ingredients": normalized_ingredients,
        "recipes": quick_recipes
    }
