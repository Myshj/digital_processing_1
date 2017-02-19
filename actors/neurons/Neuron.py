from actor_system import Actor
from actor_system.messages import Message
from actor_system.broadcasters import Broadcaster
from actor_system.broadcasters.messages import Broadcast
from .messages import ReceiveSignal, SignalTransmitted
import math


class Neuron(Actor):
    """
    Представляет собой простейший искуственный нейрон.
    """

    def __init__(self):
        super().__init__()
        self.signal_transmitted_broadcaster = Broadcaster()

    def on_message(self, message: Message):
        if isinstance(message, ReceiveSignal):
            self.on_receive_signal(value=message.value)

    def on_receive_signal(self, value: float):
        """
        Выполняется каждый раз при получении команды на передачу сигнала.
        :param float value: Входное значение сигнала.
        :return:
        """
        self._transmit_signal(value=value)

    def _transmit_signal(self, value: float):
        """
        Передача сигнала.
        :param float value: Входное значение сигнала.
        :return:
        """
        self.signal_transmitted_broadcaster.tell(
            Broadcast(
                sender=self,
                message=SignalTransmitted(
                    sender=self,
                    neuron=self,
                    input_value=value,
                    output_value=self._transmission_function(value=value)
                )
            )
        )

    def _transmission_function(self, value: float):
        """
        Преобразовывает сигнал по некоторому закону.
        :param float value: Входное значение сигнала.
        :return float: Значение сигнала после преобразования.
        """
        return 1 / (1 + math.exp(-value))
