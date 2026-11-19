import base64
from datetime import datetime

from decorators import (
    Base64Decorator,
    DateDecorator,
    HeaderDecorator,
    SignatureDecorator,
)
from messages import Message


def test_header_decorator_prepends_header() -> None:
    message = HeaderDecorator(Message("текст"), "Заголовок")

    assert message.render() == "Заголовок\nтекст"


def test_signature_decorator_appends_signature() -> None:
    message = SignatureDecorator(Message("текст"), "Подпись")

    assert message.render() == "текст\nПодпись"


def test_date_decorator_appends_explicit_date() -> None:
    message = DateDecorator(Message("текст"), datetime(2026, 12, 31))

    assert message.render() == "текст\n31.12.2026"


def test_date_decorator_appends_today_by_default() -> None:
    expected = f"текст\n{datetime.now().strftime('%d.%m.%Y')}"

    assert DateDecorator(Message("текст")).render() == expected


def test_base64_decorator_encodes_whole_text() -> None:
    encoded = Base64Decorator(Message("С наступающим Новым годом!")).render()

    assert base64.b64decode(encoded).decode("utf-8") == "С наступающим Новым годом!"


def test_full_chain_combination() -> None:
    message = Base64Decorator(
        DateDecorator(
            SignatureDecorator(HeaderDecorator(Message("текст"), "Заголовок"), "Подпись"),
            datetime(2026, 12, 31),
        )
    )

    decoded = base64.b64decode(message.render()).decode("utf-8")

    assert decoded == "Заголовок\nтекст\nПодпись\n31.12.2026"
