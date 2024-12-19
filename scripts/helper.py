import json

from letta.schemas.letta_message import LettaMessageUnion


def print_messages(messages: list[LettaMessageUnion]):
    print("==" * 20)
    for msg in messages:
        content = _get_content(msg)
        if content is None:
            continue
        print(f"{msg.message_type.upper()}\n{content}")
        print("--" * 20)
    print("==" * 20)


def _get_content(message: LettaMessageUnion):
    match message.message_type:
        case "system_message" | "user_message":
            return message.message
        case "function_call":
            args = json.loads(message.function_call.arguments)
            return f"[{message.function_call.name}]\n{args}"
        case "internal_monologue":
            return message.internal_monologue
        case _:
            return None
