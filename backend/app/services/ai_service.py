import base64
import json
from openai import OpenAI
from app.config import OPENAI_API_KEY

client = OpenAI(api_key=OPENAI_API_KEY)


def image_to_base64(image_bytes: bytes) -> str:
    return base64.b64encode(image_bytes).decode("utf-8")


async def extract_ingredients(image_bytes: bytes) -> list[str]:
    image_base64 = image_to_base64(image_bytes)

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        response_format={
            "type": "json_schema",
            "json_schema": {
                "name": "ingredient_list",
                "schema": {
                    "type": "object",
                    "properties": {
                        "ingredients": {
                            "type": "array",
                            "items": {"type": "string"}
                        }
                    },
                    "required": ["ingredients"],
                    "additionalProperties": False
                },
                "strict": True
            }
        },
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": (
                            "You are a vision-based food analysis agent. "
                            "List ONLY visible food ingredients from the fridge image. "
                            "Do not guess hidden items."
                        )
                    },
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/jpeg;base64,{image_base64}"
                        }
                    }
                ]
            }
        ]
    )

    data = json.loads(response.choices[0].message.content)
    return data["ingredients"]

async def generate_recipes(ingredients: list[str]):
    prompt = (
        "You are a professional home chef.\n"
        f"Available ingredients: {ingredients}\n\n"
        "Suggest 3 to 5 dishes that:\n"
        "- Can be cooked in 30 minutes or less\n"
        "- Are simple home recipes\n"
        "- Use mostly the available ingredients\n\n"
        "Return ONLY valid JSON following this schema:\n"
        "{"
        '"recipes": ['
        '{'
        '"dish": string, '
        '"time_minutes": number (<=30), '
        '"difficulty": "easy" | "medium", '
        '"uses": [string], '
        '"missing_optional": [string], '
        '"quick_steps": [string]'
        '}'
        ']'
        "}"
    )

    response = client.chat.completions.create(
        model="gpt-4o",
        response_format={
            "type": "json_schema",
            "json_schema": {
                "name": "recipe_list",
                "schema": {
                    "type": "object",
                    "properties": {
                        "recipes": {
                            "type": "array",
                            "items": {
                                "type": "object",
                                "properties": {
                                    "dish": {"type": "string"},
                                    "time_minutes": {"type": "number"},
                                    "difficulty": {"type": "string"},
                                    "uses": {
                                        "type": "array",
                                        "items": {"type": "string"}
                                    },
                                    "missing_optional": {
                                        "type": "array",
                                        "items": {"type": "string"}
                                    },
                                    "quick_steps": {
                                        "type": "array",
                                        "items": {"type": "string"}
                                    }
                                },
                                "required": [
                                    "dish",
                                    "time_minutes",
                                    "difficulty",
                                    "uses",
                                    "missing_optional",
                                    "quick_steps"
                                ],
                                "additionalProperties": False
                            }
                        }
                    },
                    "required": ["recipes"],
                    "additionalProperties": False
                },
                "strict": True
            }
        },
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return json.loads(response.choices[0].message.content)["recipes"]
