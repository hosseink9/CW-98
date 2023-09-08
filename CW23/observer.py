from __future__ import annotations
from abc import ABC, abstractmethod
from random import randrange
from typing import List


class Subject(ABC):
    """
    The Subject interface declares a set of methods for managing subscribers.
    """

    @abstractmethod
    def register(self, observer: Observer) -> None:
        """
        Attach an observer to the subject.
        """
        pass

    @abstractmethod
    def unregister(self, observer: Observer) -> None:
        """
        Detach an observer from the subject.
        """
        pass

    @abstractmethod
    def notify(self) -> None:
        """
        Notify all observers about an event.
        """
        pass


class WeatherStaion(Subject):

    _state: dict = {'temp':None,'hum':None}


    _observers: List[Observer] = []


    def register(self, observer: Observer) -> None:
        print("Subject: Attached an observer.")
        self._observers.append(observer)

    def unregister(self, observer: Observer) -> None:
        self._observers.remove(observer)
        print("Subject: Unattached an observer.")

    def notify(self) -> None:

        print("Subject: Notifying observers...")
        for observer in self._observers:
            observer.update(self)

    def some_business_logic(self) -> None:

        print("\nSubject: I'm doing something important.")

        self._state['temp'] = randrange(30, 100)
        self._state['hum'] = randrange(70, 90)

        print(f"Subject: My state has just changed to: {self._state}")
        self.notify()


class Observer(ABC):

    @abstractmethod
    def update(self, subject: Subject) -> None:
        pass



class TemperatureDisplay(Observer):
    def update(self, subject: Subject) -> None:

        if subject._state['temp']>60:
            print('its hot')
        else:
            print('cold')


class HumidityDisplay(Observer):
    def update(self, subject: Subject) -> None:
        hum = subject._state['hum']
        print(f'{hum=}')


if __name__ == "__main__":
    # The client code.

    subject = WeatherStaion()
    print('state'.center(100, '-'))

    observer_a = TemperatureDisplay()
    subject.register(observer_a)
    print('state'.center(100, '-'))

    observer_b = HumidityDisplay()
    subject.register(observer_b)
    print('state'.center(100, '-'))

    subject.some_business_logic()
    print('state'.center(100, '-'))

    subject.some_business_logic()
    print('state'.center(100, '-'))

    subject.unregister(observer_a)
    print('state'.center(100, '-'))

    subject.some_business_logic()
    print('state'.center(100, '-'))