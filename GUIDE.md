# Greeting Agent — Code Explained

A plain-English guide to every part of this agent, what it does, and why.

---

## Project Structure

```
greetingagent/
├── .bedrock_agentcore.yaml   ← Config file: tells AgentCore how to run/deploy your agent
├── .gitignore                ← Config file: tells Git which files to ignore
├── pyproject.toml            ← Config file: lists dependencies (the "shopping list")
└── src/
    ├── main.py               ← The brain: receives messages, creates agent, responds
    ├── tools.py              ← The skills: functions the agent can call
    └── model/
        └── load.py           ← The model loader: connects to Claude AI via Bedrock
```

### Terminology

| Term | Meaning |
|------|---------|
| File | The most basic unit. Any file on disk (`.py`, `.toml`, `.yaml`, etc.) |
| Module | A `.py` file that contains reusable code you can import |
| Package | A folder of modules that work together |
| Library | A package someone else built that you install and use (e.g. `strands-agents`) |

---

## The Two Frameworks

This agent uses two frameworks working together:

| Framework | Role | Analogy |
|-----------|------|---------|
| **Strands Agents** | Builds the agent (brain + skills) | The chef who cooks the food |
| **Bedrock AgentCore** | Runs and hosts the agent | The restaurant that serves the food |

- **Strands** handles the thinking — how the agent reasons, picks tools, generates responses.
- **AgentCore** handles the plumbing — how messages get in and responses get out.

They're independent but designed to work together.

---

## main.py — Line by Line

### Section 1: Docstring
```python
"""
Greeting Agent - A friendly agent with fun skills
Built with AWS AgentCore + Strands
"""
```
A comment for humans. Describes what this file does. Does nothing when the code runs.

### Section 2: Imports
```python
from strands import Agent
from bedrock_agentcore.runtime import BedrockAgentCoreApp
from model.load import load_model
from tools import greet_in_language, fun_fact_today, give_compliment, cheers_around_the_world
```

The "shopping" section — grabbing things you need from other places:

| Import | What it is | Why you need it |
|--------|-----------|-----------------|
| `Agent` | Class from `strands` library | The actual AI agent that thinks and responds |
| `BedrockAgentCoreApp` | Class from `bedrock-agentcore` library | The server that runs your agent |
| `load_model` | Function from your `model/load.py` | Loads the Claude AI model (the brain) |
| `greet_in_language`, etc. | Functions from your `tools.py` | The skills your agent can use |

Analogy: `Agent` is the person, `load_model` gives them a brain, `tools` give them skills, `BedrockAgentCoreApp` gives them a workplace.

### Section 3: Create the App
```python
app = BedrockAgentCoreApp()
log = app.logger
```

- `app` — Creates the AgentCore application (the server that listens for messages).
- `log` — A logger for debugging. Like `print()` but with timestamps and levels.

### Section 4: The Entry Point
```python
@app.entrypoint
async def invoke(payload, context):
```

- `@app.entrypoint` — A "decorator." Tells AgentCore: "when a message comes in, run THIS function." Like a sign on a door that says "start here."
- `async def` — Defines a function that can wait for slow things (like AI responses) without freezing.
- `invoke` — The function name. Convention, could be anything.
- `payload` — The incoming message as a dictionary. Example: `{"prompt": "Say hi to Maria in French"}`
- `context` — Extra info about the request from AgentCore (session info, etc.)

### Section 5: Get the User's Message
```python
user_prompt = payload.get("prompt", "Hello")
log.info(f"Received prompt: {user_prompt}")
```

- `payload.get("prompt", "Hello")` — Grabs the `"prompt"` value from the payload. If missing, defaults to `"Hello"`. Safe way to read from a dictionary.
- `log.info(...)` — Logs what came in for debugging.

### Section 6: Create the Agent
```python
agent = Agent(
    model=load_model(),
    system_prompt="""...""",
    tools=[greet_in_language, fun_fact_today, give_compliment, cheers_around_the_world],
)
```

Assembling the agent from 3 parts:

| Part | What it does |
|------|-------------|
| `model=load_model()` | The brain — which AI model to use (Claude via Bedrock) |
| `system_prompt="..."` | The personality — secret instructions the user never sees |
| `tools=[...]` | The skills — functions the agent is allowed to call |

### Section 7: Stream the Response
```python
stream = agent.stream_async(user_prompt)

async for event in stream:
    if "data" in event and isinstance(event["data"], str):
        yield event["data"]
```

- `stream_async(user_prompt)` — Sends the message to the agent, gets back a stream (response comes in chunks, like watching someone type).
- `async for event in stream` — Loops through each chunk as it arrives.
- `yield event["data"]` — Sends each chunk back to the user immediately. `yield` is like `return` but doesn't stop the function — it keeps sending more.

### Section 8: Run It
```python
if __name__ == "__main__":
    app.run()
```

"If someone runs this file directly, start the server." The ignition key.

---

## tools.py — The Skills

Each tool is just a regular Python function with:
1. A clear name
2. A docstring (description in triple quotes) — the agent reads this to know when to use the tool
3. Parameters with type hints — so the agent knows what inputs to provide
4. A return value (dictionary) — the result the agent gets back

| Tool | What it does |
|------|-------------|
| `greet_in_language(name, language)` | Says hello in 10 different languages |
| `fun_fact_today()` | Shares a fun fact about today's date |
| `give_compliment(name)` | Gives a random personalized compliment |
| `cheers_around_the_world()` | Shows how to say "cheers" in 12 cultures |

The agent decides which tool to use based on what the user asks. You don't write if/else logic for that — the AI figures it out from the docstrings.

---

## model/load.py — The Brain Loader

```python
MODEL_ID = "global.anthropic.claude-sonnet-4-5-20250929-v1:0"

def load_model():
    return BedrockModel(model_id=MODEL_ID)
```

Connects to Claude (the AI model) through AWS Bedrock. This is what gives your agent the ability to understand language and reason.

---

## Config Files

### pyproject.toml
Lists your project name, version, and dependencies. When you run `pip install`, it reads this file to know what libraries to download.

### .bedrock_agentcore.yaml
Tells AgentCore everything about your agent: what language it's in, where the code lives, how to deploy it, what AWS settings to use.

### .gitignore
Lists files that should NOT be saved to your repository (like `.venv/`, `__pycache__/`, `.env`). These are generated files or secrets that don't belong in version control.

---

## The Agent Pattern

Every AgentCore agent follows this skeleton:

```
1. Import your stuff
2. Create the app (BedrockAgentCoreApp)
3. Define an entry point function that:
   a. Reads the user's message from payload
   b. Creates an Agent with a model, personality, and tools
   c. Sends the message to the agent
   d. Streams the response back
4. Run the app
```

The only things that change between agents are the **system prompt** and the **tools**. That's what makes each agent unique.

---

## Local vs Deployed

The same code runs in both places. The difference is WHERE:

| | Local (your Mac) | Deployed (AWS) |
|---|---|---|
| Who can use it | Only you | Anyone with access |
| Always running? | Only when terminal is open | Yes, 24/7 |
| Address | `localhost:8080` | A public AWS URL |
| Scales? | One user at a time | Thousands of users |
| Survives laptop closing? | No | Yes |

---

## The Full Lifecycle

```
Step 1: Write the code         → Files on your laptop
Step 2: Test locally           → Run it, make sure it works
Step 3: Push to a repository   → Save it online (backup + collaboration)
Step 4: Build                  → Package it for deployment
Step 5: Deploy                 → Put it on AWS servers, always running
```
