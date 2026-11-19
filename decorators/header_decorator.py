from interfaces import BaseMessage

from .message_decorator import MessageDecorator


class HeaderDecorator(MessageDecorator):
    def __init__(self, message: BaseMessage, header: str) -> None:
        super().__init__(message)
        self._header = header

    def render(self) -> str:
        return f"{self._header}\n{self._message.render()}"
