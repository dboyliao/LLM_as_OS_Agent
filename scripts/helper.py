from letta.schemas.message import LettaMessageUnion


def print_messages(messages: list[LettaMessageUnion]):
    print("==" * 20)
    for msg in messages:
        print(f"{msg.message_type.upper()}\n{msg.text}")
    print("==" * 20)


def _get_content(message: LettaMessageUnion):
    if message.message_type in ["system_message", "user_message"]:
        return message.message
    elif message.message_type == "internal_monologue":
        return message.internal_monologue
    else:
        ...
