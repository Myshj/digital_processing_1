from actor_system.messages import Message
from actor_system import Actor


class ReceiveSignal(Message):
    """
    Говорит нейрону, что он должен получить сигнал и отреагировать на него.
    """

    def __init__(self, sender: Actor, value: float):
        """
        Конструктор.
        :param Actor sender: Адресант сообщения.
        :param float value: Значение сигнала.
        """
        super().__init__(sender)
        self.value = value
