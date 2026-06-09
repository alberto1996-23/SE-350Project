from abc import ABC, abstractmethod

class OrderObserver(ABC):
    @abstractmethod
    def update(self, order: "Order") -> None:
        """I use this as the observer hook every display has to respond with."""
        pass