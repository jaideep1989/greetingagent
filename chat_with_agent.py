"""
Interactive chat with your greeting agent.
Type 'quit' or 'exit' to stop.
"""
import requests

AGENT_URL = "http://localhost:8080/invocations"


def chat():
    print("👋 Greeting Agent - Interactive Chat")
    print("=" * 50)
    print("Try things like:")
    print("  - Say hi to Maria in Japanese")
    print("  - Give me a fun fact about today")
    print("  - Compliment my friend Alex")
    print("  - How do you say cheers around the world?")
    print("Type 'quit' or 'exit' to stop\n")

    while True:
        user_input = input("You: ").strip()

        if user_input.lower() in ["quit", "exit", "q"]:
            print("\n👋 Goodbye!")
            break

        if not user_input:
            continue

        print("Agent: ", end="", flush=True)

        try:
            response = requests.post(
                AGENT_URL,
                json={"prompt": user_input},
                stream=True,
                timeout=30,
            )

            for line in response.iter_lines():
                if line:
                    decoded = line.decode("utf-8")
                    if decoded.startswith("data: "):
                        content = decoded[6:]
                        if content.startswith('"') and content.endswith('"'):
                            content = content[1:-1]
                        print(content, end="", flush=True)

            print("\n")

        except requests.exceptions.ConnectionError:
            print("\n❌ Can't connect to agent!")
            print("Make sure dev server is running: agentcore dev\n")
            break
        except Exception as e:
            print(f"\n❌ Error: {e}\n")


if __name__ == "__main__":
    chat()
