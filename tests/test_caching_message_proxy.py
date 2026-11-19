from proxies import CachingMessageProxy


def test_first_render_delegates_and_repeats_use_cache(recording_message) -> None:
    proxy = CachingMessageProxy(recording_message)

    assert recording_message.render_calls == 0
    assert proxy.render() == "текст сообщения"
    assert recording_message.render_calls == 1
    assert proxy.render() == "текст сообщения"
    assert recording_message.render_calls == 1
