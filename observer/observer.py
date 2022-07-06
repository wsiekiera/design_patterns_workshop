from __future__ import annotations
from abc import ABC, abstractmethod


class Subject(ABC):
    """
    The Subject interface declares a set of methods for managing subscribers.
    """

    def __init__(self, event_type):
        self._event_type = event_type
        self._observers = []

    @abstractmethod
    def attach(self, observer: Observer) -> None:
        """
        Attach an observer to the subject.
        """
        pass

    @abstractmethod
    def detach(self, observer: Observer) -> None:
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


class ConcreteSubject(Subject):

    def attach(self, observer: Observer) -> None:
        print("Subject: Attached an observer.")
        self._observers.append(observer)

    def detach(self, observer: Observer) -> None:
        self._observers.remove(observer)

    """
    The subscription management methods.
    """

    def notify(self) -> None:
        """
        Trigger an update in each subscriber.
        """

        print("Subject: Notifying observers...")
        for observer in self._observers:
            observer.update(self)


class Observer(ABC):
    """
    The Observer interface declares the update method, used by subjects.
    """

    @abstractmethod
    def update(self, subject: Subject) -> None:
        """
        Receive update from subject.
        """
        pass


"""
Concrete Observers react to the updates issued by the Subject they had been
attached to.
"""


class MailObserver(Observer):
    def update(self, subject: Subject) -> None:
        print(f'[MAIL] Received update from subject with event_type={subject._event_type}')


class SmsObserver(Observer):
    def update(self, subject: Subject) -> None:
        print(f'[SMS] Received update from subject with event_type={subject._event_type}')


class PushObserver(Observer):
    def update(self, subject: Subject) -> None:
        print(f'[PUSH] Received update from subject with event_type={subject._event_type}')


if __name__ == "__main__":
    # The client code.

    accountsSubject = ConcreteSubject('accounts')
    transactionSubject = ConcreteSubject('transactions')

    sms_observer = SmsObserver()
    push_observer = PushObserver()
    mail_observer = MailObserver()

    accountsSubject.attach(sms_observer)
    accountsSubject.attach(push_observer)
    transactionSubject.attach(mail_observer)
    transactionSubject.attach(sms_observer)

    with open('observer_data.txt', 'r') as file:
        lines = file.readlines()
        for line in lines:
            if len(line) > 0:
                words = line.split(',')
                event_type = words[0]
                cunbr = words[1]
                if event_type.startswith('account'):
                    accountsSubject.notify()
                elif event_type.startswith('payment'):
                    transactionSubject.notify()
