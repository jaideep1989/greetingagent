"""
Greeting Agent - A friendly agent with fun skills
Built with AWS AgentCore + Strands
"""
from strands import Agent
from bedrock_agentcore.runtime import BedrockAgentCoreApp
from model.load import load_model
from tools import greet_in_language, fun_fact_today, give_compliment, cheers_around_the_world

# Create the AgentCore app
app = BedrockAgentCoreApp()
log = app.logger


@app.entrypoint
async def invoke(payload, context):
    """
    Main entry point — receives a user message and responds.

    Args:
        payload: Contains the user's prompt
        context: Runtime context from AgentCore
    """
    user_prompt = payload.get("prompt", "Hello")

    log.info(f"Received prompt: {user_prompt}")

    agent = Agent(
        model=load_model(),
        system_prompt="""
        You are a warm, friendly greeting agent. You love making people smile.

        Your skills:
        - greet_in_language: Greet someone by name in different languages
        - fun_fact_today: Share a fun fact about today's date
        - give_compliment: Give someone a personalized compliment
        - cheers_around_the_world: Show how to say 'cheers' in many cultures

        Use your tools whenever they're relevant. Be cheerful and conversational.
        If someone just says hi, greet them and offer to show off your skills.
        """,
        tools=[greet_in_language, fun_fact_today, give_compliment, cheers_around_the_world],
    )

    stream = agent.stream_async(user_prompt)

    async for event in stream:
        if "data" in event and isinstance(event["data"], str):
            yield event["data"]


if __name__ == "__main__":
    app.run()
