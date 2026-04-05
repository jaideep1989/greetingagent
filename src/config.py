"""
Configuration for the Greeting Agent
"""
import os

# Agent configuration
AGENT_NAME = os.getenv("AGENT_NAME", "GreetingAgent")
AGENT_VERSION = os.getenv("AGENT_VERSION", "0.2.0")
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")

# Model configuration
DEFAULT_MODEL_ID = os.getenv(
    "MODEL_ID",
    "global.anthropic.claude-sonnet-4-5-20250929-v1:0"
)
MAX_TOKENS = int(os.getenv("MAX_TOKENS", "1024"))
TEMPERATURE = float(os.getenv("TEMPERATURE", "0.7"))

# Feature flags
ENABLE_WEATHER = os.getenv("ENABLE_WEATHER", "true").lower() == "true"
ENABLE_QUOTES = os.getenv("ENABLE_QUOTES", "true").lower() == "true"
