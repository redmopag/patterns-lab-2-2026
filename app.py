from datetime import datetime

from decorators import (
    Base64Decorator,
    DateDecorator,
    HeaderDecorator,
    SignatureDecorator,
)
from messages import Message
from proxies import CachingMessageProxy, ProtectedMessageProxy
from security import AccessPolicy, UserContext


def main() -> None:
    message = Message("С наступающим Новым годом!")
    print("Базовый компонент:")
    print(message.render())

    decorated = DateDecorator(
        SignatureDecorator(
            HeaderDecorator(message, "Праздничное поздравление"),
            "Команда курса",
        ),
        datetime(2026, 12, 31),
    )
    print()
    print("Цепочка декораторов:")
    print(decorated.render())

    print()
    print("Base64 поверх цепочки:")
    print(Base64Decorator(decorated).render())

    policy = AccessPolicy("reader")
    reader = UserContext.of("alice", "reader")
    guest = UserContext.of("bob", "guest")

    print()
    print("Proxy: доступ разрешён:")
    print(ProtectedMessageProxy(decorated, policy, reader).render())

    print()
    print("Proxy: доступ запрещён:")
    try:
        ProtectedMessageProxy(decorated, policy, guest).render()
    except PermissionError as error:
        print(f"PermissionError: {error}")

    print()
    print("Совместная работа Proxy (защита снаружи, кэш внутри):")
    cache = CachingMessageProxy(decorated)
    shared_reader = ProtectedMessageProxy(cache, policy, reader)
    shared_guest = ProtectedMessageProxy(cache, policy, guest)
    print(shared_reader.render())
    print(shared_reader.render())
    try:
        shared_guest.render()
    except PermissionError as error:
        print(f"PermissionError: {error}")


if __name__ == "__main__":
    main()
