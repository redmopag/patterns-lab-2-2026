import pytest

from proxies import CachingMessageProxy, ProtectedMessageProxy
from security import AccessPolicy, UserContext


def test_render_returns_real_text_when_allowed(recording_message) -> None:
    proxy = ProtectedMessageProxy(
        recording_message, AccessPolicy("reader"), UserContext.of("alice", "reader")
    )

    assert proxy.render() == "текст сообщения"


def test_render_denied_raises_and_skips_subject(recording_message) -> None:
    proxy = ProtectedMessageProxy(
        recording_message, AccessPolicy("reader"), UserContext.of("bob", "guest")
    )

    with pytest.raises(PermissionError):
        proxy.render()

    assert recording_message.render_calls == 0


def test_composition_checks_access_before_cache(recording_message) -> None:
    cache = CachingMessageProxy(recording_message)
    reader = ProtectedMessageProxy(
        cache, AccessPolicy("reader"), UserContext.of("alice", "reader")
    )
    guest = ProtectedMessageProxy(
        cache, AccessPolicy("reader"), UserContext.of("bob", "guest")
    )

    reader.render()
    reader.render()
    with pytest.raises(PermissionError):
        guest.render()

    assert recording_message.render_calls == 1
