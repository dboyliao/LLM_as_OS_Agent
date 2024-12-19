from helper import print_messages

import letta
from letta import ChatMemory, EmbeddingConfig, LLMConfig

client = letta.create_client()
agent_state = client.create_agent(
    memory=ChatMemory(
        human="My name is Dboy.",
        persona="You are an AI agent named Lutta. You like to talk like a pirate, like captain Jack Sparrow.",
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
print_messages(response.messages)
response = client.send_message(
    agent_id=agent_state.id,
    message="Save the information that 'I have changed my name as BBoy' to archival memory",
    role="user",
)
print_messages(response.messages)
passage = client.insert_archival_memory(
    agent_state.id, "BBoy's favorite singer is Olivia Ong"
)
print(passage)
response = client.send_message(
    agent_id=agent_state.id, role="user", message="Who is my favorite singer?"
)
print_messages(response.messages)
