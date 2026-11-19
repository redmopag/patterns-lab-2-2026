import base64

from .message_decorator import MessageDecorator


class Base64Decorator(MessageDecorator):
    def render(self) -> str:
        # UTF-8-текст превращается в байты, а Base64-результат состоит только
        # из ascii-символов и безопасно возвращается строкой.
        encoded = self._message.render().encode("utf-8")
        return base64.b64encode(encoded).decode("ascii")
