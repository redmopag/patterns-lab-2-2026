import pytest

from interfaces import BaseMessage


class RecordingMessage(BaseMessage):
    def __init__(self, text: str) -> None:
        self._text = text
        self.render_calls = 0

    def render(self) -> str:
        self.render_calls += 1
        return self._text


@pytest.fixture
def recording_message() -> RecordingMessage:
    return RecordingMessage("текст сообщения")
