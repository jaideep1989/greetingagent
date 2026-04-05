from strands.models import BedrockModel
from config import DEFAULT_MODEL_ID, MAX_TOKENS, TEMPERATURE


def load_model() -> BedrockModel:
    """
    Get Bedrock model client.
    Uses IAM authentication via the execution role.
    Configuration loaded from config.py / environment variables.
    """
    return BedrockModel(
        model_id=DEFAULT_MODEL_ID,
        max_tokens=MAX_TOKENS,
        temperature=TEMPERATURE,
    )
