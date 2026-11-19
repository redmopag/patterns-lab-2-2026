from interfaces import BaseMessage

from .message_decorator import MessageDecorator


class SignatureDecorator(MessageDecorator):
    def __init__(self, message: BaseMessage, signature: str) -> None:
        super().__init__(message)
        self._signature = signature

    def render(self) -> str:
        return f"{self._message.render()}\n{self._signature}"
