from interfaces import BaseMessage
from security import AccessPolicy, UserContext


class ProtectedMessageProxy(BaseMessage):
    """Пользователь внедряется конструктором: сигнатура render() зафиксирована
    интерфейсом BaseMessage и не позволяет передавать контекст вызова."""

    def __init__(self, message: BaseMessage, policy: AccessPolicy, user: UserContext) -> None:
        self._message = message
        self._policy = policy
        self._user = user

    def render(self) -> str:
        if not self._policy.is_allowed(self._user):
            raise PermissionError(
                f"Пользователю '{self._user.username}' не хватает роли для доступа к сообщению"
            )
        return self._message.render()
