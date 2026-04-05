"""
Skills for the Greeting Agent
"""
import random
import logging
from datetime import datetime

logger = logging.getLogger(__name__)


def greet_in_language(name: str, language: str) -> dict:
    """
    Greets a person by name in the specified language.

    Args:
        name: The person's name to greet
        language: The language to greet in (english, spanish, french, japanese,
                  german, italian, portuguese, korean, arabic, hindi)

    Returns:
        Dictionary with the greeting
    """
    greetings = {
        "english": "Hello",
        "spanish": "¡Hola",
        "french": "Bonjour",
        "japanese": "こんにちは (Konnichiwa)",
        "german": "Hallo",
        "italian": "Ciao",
        "portuguese": "Olá",
        "korean": "안녕하세요 (Annyeonghaseyo)",
        "arabic": "مرحبا (Marhaba)",
        "hindi": "नमस्ते (Namaste)",
    }

    lang = language.lower().strip()
    logger.info(f"Greeting {name} in {lang}")
    greeting = greetings.get(lang)

    if not greeting:
        available = ", ".join(greetings.keys())
        logger.warning(f"Unknown language requested: {language}")
        return {"error": f"Unknown language: {language}. Available: {available}"}

    return {
        "greeting": f"{greeting}, {name}!",
        "language": lang,
    }


def fun_fact_today() -> dict:
    """
    Returns a fun fact about today's date (month and day).

    Returns:
        Dictionary with today's date and a fun fact
    """
    facts = {
        (1, 1): "New Year's Day — the most widely celebrated holiday worldwide.",
        (2, 14): "Valentine's Day originated from a Roman festival called Lupercalia.",
        (3, 14): "Pi Day! Because 3/14 matches 3.14, the start of pi.",
        (4, 22): "Earth Day — first celebrated in 1970 with 20 million Americans.",
        (7, 4): "US Independence Day — about 150 million hot dogs are eaten today.",
        (10, 31): "Halloween — Americans spend about $10 billion on it each year.",
        (12, 25): "Christmas — 'Jingle Bells' was originally written for Thanksgiving.",
    }

    now = datetime.now()
    key = (now.month, now.day)
    fact = facts.get(key, f"On this day in history, something amazing probably happened. "
                          f"Every day is worth celebrating!")

    return {
        "date": now.strftime("%B %d"),
        "day_of_week": now.strftime("%A"),
        "fun_fact": fact,
    }


def give_compliment(name: str) -> dict:
    """
    Generates a personalized compliment for someone.

    Args:
        name: The person's name to compliment

    Returns:
        Dictionary with a compliment
    """
    compliments = [
        f"{name}, you have a great sense of humor!",
        f"{name}, your positive energy is contagious!",
        f"{name}, you make the world a better place just by being in it.",
        f"{name}, you're braver than you believe and stronger than you seem.",
        f"{name}, your creativity inspires everyone around you!",
        f"{name}, you have an amazing ability to make people feel welcome.",
        f"{name}, your determination is truly admirable!",
        f"{name}, you light up every room you walk into.",
    ]

    return {"compliment": random.choice(compliments)}


def cheers_around_the_world() -> dict:
    """
    Returns how to say 'cheers' in different cultures, with a random featured one.

    Returns:
        Dictionary with cheers in various languages and a featured pick
    """
    cheers = {
        "English": "Cheers!",
        "Spanish": "¡Salud!",
        "French": "Santé!",
        "German": "Prost!",
        "Italian": "Cin cin!",
        "Japanese": "乾杯 (Kanpai)!",
        "Korean": "건배 (Geonbae)!",
        "Portuguese": "Saúde!",
        "Russian": "За здоровье (Za zdorovye)!",
        "Mandarin": "干杯 (Gānbēi)!",
        "Swedish": "Skål!",
        "Irish": "Sláinte!",
    }

    featured_lang = random.choice(list(cheers.keys()))

    return {
        "featured": {
            "language": featured_lang,
            "cheers": cheers[featured_lang],
        },
        "all_cheers": cheers,
    }


def weather_greeting(city: str) -> dict:
    """
    Generates a weather-appropriate greeting for a city.
    Uses simulated weather data for demo purposes.

    Args:
        city: The city name to generate a weather greeting for

    Returns:
        Dictionary with city, weather condition, and a themed greeting
    """
    weather_conditions = [
        {"condition": "sunny", "temp": 28, "greeting": f"What a beautiful sunny day in {city}! Perfect for a walk."},
        {"condition": "rainy", "temp": 15, "greeting": f"It's raining in {city} — grab an umbrella and stay cozy!"},
        {"condition": "cloudy", "temp": 20, "greeting": f"Cloudy skies over {city} today, but your smile brightens things up!"},
        {"condition": "snowy", "temp": -2, "greeting": f"Snow is falling in {city}! Time for hot cocoa and warm vibes."},
        {"condition": "windy", "temp": 18, "greeting": f"Hold onto your hat in {city} — it's a breezy one today!"},
    ]

    logger.info(f"Generating weather greeting for {city}")
    weather = random.choice(weather_conditions)

    return {
        "city": city,
        "condition": weather["condition"],
        "temperature_c": weather["temp"],
        "greeting": weather["greeting"],
    }
