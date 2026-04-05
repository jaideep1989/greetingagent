# Greeting Agent 🤖👋

A warm, friendly AI agent built with AWS AgentCore + Strands that greets users
and makes them smile with a variety of fun tools.

## Features

- **Multi-language Greetings** — Greet anyone in 10+ languages
- **Fun Facts** — Share interesting facts about today's date
- **Compliments** — Generate personalized compliments
- **Cheers Around the World** — Learn how to say cheers in 12 cultures
- **Weather Greetings** — Get weather-themed greetings for any city
- **Motivational Quotes** — Inspiring quotes filtered by topic

## Quick Start

```bash
# Create and activate virtual environment
python -m venv .venv
source .venv/bin/activate

# Install dependencies
pip install -e .

# Run locally
python src/main.py
```

## Configuration

Set environment variables or edit `src/config.py`:

| Variable | Default | Description |
|----------|---------|-------------|
| `MODEL_ID` | `global.anthropic.claude-sonnet-4-5-20250929-v1:0` | Bedrock model |
| `MAX_TOKENS` | `1024` | Max response tokens |
| `TEMPERATURE` | `0.7` | Model temperature |
| `ENABLE_WEATHER` | `true` | Enable weather tool |
| `ENABLE_QUOTES` | `true` | Enable quotes tool |

## Testing

```bash
pytest tests/ -v
```

## Architecture

```
src/
├── main.py          # Agent entrypoint (AgentCore)
├── config.py        # Centralized configuration
├── tools.py         # All agent tools/skills
└── model/
    └── load.py      # Bedrock model loader
```
