from datetime import datetime

from interfaces import BaseMessage

from .message_decorator import MessageDecorator

DATE_FORMAT = "%d.%m.%Y"


class DateDecorator(MessageDecorator):
    def __init__(self, message: BaseMessage, date: datetime | None = None) -> None:
        super().__init__(message)
        self._date = date

    def render(self) -> str:
        date = self._date or datetime.now()
        return f"{self._message.render()}\n{date.strftime(DATE_FORMAT)}"
