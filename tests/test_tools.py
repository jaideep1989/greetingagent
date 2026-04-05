"""
Unit tests for greeting agent tools
"""
import pytest
import sys
import os

# Add src to path for imports
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from tools import greet_in_language, fun_fact_today, give_compliment, cheers_around_the_world, weather_greeting, motivational_quote


class TestGreetInLanguage:
    def test_english_greeting(self):
        result = greet_in_language("Alice", "english")
        assert "greeting" in result
        assert "Alice" in result["greeting"]
        assert result["language"] == "english"

    def test_spanish_greeting(self):
        result = greet_in_language("Bob", "spanish")
        assert "greeting" in result
        assert "Bob" in result["greeting"]

    def test_unknown_language(self):
        result = greet_in_language("Charlie", "klingon")
        assert "error" in result

    def test_case_insensitive(self):
        result = greet_in_language("Dana", "FRENCH")
        assert "greeting" in result
        assert result["language"] == "french"


class TestFunFactToday:
    def test_returns_date(self):
        result = fun_fact_today()
        assert "date" in result
        assert "day_of_week" in result
        assert "fun_fact" in result

    def test_fact_is_string(self):
        result = fun_fact_today()
        assert isinstance(result["fun_fact"], str)
        assert len(result["fun_fact"]) > 0


class TestGiveCompliment:
    def test_returns_compliment(self):
        result = give_compliment("Eve")
        assert "compliment" in result
        assert "Eve" in result["compliment"]

    def test_compliment_is_string(self):
        result = give_compliment("Frank")
        assert isinstance(result["compliment"], str)


class TestCheersAroundTheWorld:
    def test_returns_featured(self):
        result = cheers_around_the_world()
        assert "featured" in result
        assert "language" in result["featured"]
        assert "cheers" in result["featured"]

    def test_returns_all_cheers(self):
        result = cheers_around_the_world()
        assert "all_cheers" in result
        assert len(result["all_cheers"]) >= 10


class TestWeatherGreeting:
    def test_returns_city(self):
        result = weather_greeting("Seattle")
        assert result["city"] == "Seattle"

    def test_returns_condition(self):
        result = weather_greeting("Tokyo")
        assert "condition" in result
        assert "temperature_c" in result
        assert "greeting" in result


class TestMotivationalQuote:
    def test_default_topic(self):
        result = motivational_quote()
        assert "quote" in result
        assert "author" in result
        assert result["topic"] == "general"

    def test_specific_topic(self):
        result = motivational_quote("kindness")
        assert result["topic"] == "kindness"

    def test_unknown_topic_falls_back(self):
        result = motivational_quote("quantum_physics")
        assert "quote" in result  # falls back to general
