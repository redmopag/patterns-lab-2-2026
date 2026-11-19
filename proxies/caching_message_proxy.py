from interfaces import BaseMessage


class CachingMessageProxy(BaseMessage):
    def __init__(self, message: BaseMessage) -> None:
        self._message = message
        self._cached: str | None = None

    def render(self) -> str:
        if self._cached is None:
            self._cached = self._message.render()
        return self._cached
