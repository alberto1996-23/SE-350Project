from abc import ABC, abstractmethod

class OrderState(ABC):
    @abstractmethod
    def submit(self, order: "Order") -> None:
        """I use this to define what submitting means in a specific state."""
        pass

    @abstractmethod
    def send_to_kitchen(self, order: "Order") -> None:
        """I use this to define what sending to the kitchen means in a specific state."""
        pass

    @abstractmethod
    def prepare(self, order: "Order") -> None:
        """I use this to define what preparing means in a specific state."""
        pass

    @abstractmethod
    def mark_ready(self, order: "Order") -> None:
        """I use this to define what marking ready means in a specific state."""
        pass

    @abstractmethod
    def get_status_name(self) -> str:
        """I use this to return the label the order should show for this state."""
        pass