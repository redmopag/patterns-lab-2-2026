from interfaces import BaseMessage


class MessageDecorator(BaseMessage):
    def __init__(self, message: BaseMessage) -> None:
        self._message = message

    def render(self) -> str:
        return self._message.render()
