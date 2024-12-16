from helper import print_messages

import letta
from letta import ChatMemory, EmbeddingConfig, LLMConfig

client = letta.create_client()
agent_state = client.create_agent(
    memory=ChatMemory(
        human="My name is Dboy.",
        persona="You are a cool and chill AI agent named Lutta.",
    ),
    llm_config=LLMConfig(
        model="qwq:latest",
        model_endpoint_type="ollama",
        model_endpoint="http://localhost:11434",
        context_window=8192,
    ),
    embedding_config=EmbeddingConfig.default_config(model_name="letta"),
)

response = client.send_message(agent_id=agent_state.id, message="hello!", role="user")
