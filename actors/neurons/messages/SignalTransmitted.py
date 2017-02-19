from actor_system.messages import Message
from actor_system import Actor
from actors.neurons import Neuron


class SignalTransmitted(Message):
    """
    Сообщение от нейрона о выдаче выходного сигнала.
    """

    def __init__(self, sender: Actor, neuron: Neuron, input_value: float, output_value: float):
        """
        Конструктор.
        :param Actor sender: Адресант сообщения.
        :param Neuron neuron: Нейрон, выдавший сигнал.
        :param float input_value: Входное значение сигнала.
        :param float output_value: Выходное значение сигнала.
        """
        super().__init__(sender)
        self.neuron = neuron
        self.input_value = input_value
        self.output_value = output_value
