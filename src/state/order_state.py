from abc import ABC, abstractmethod

class OrderState(ABC):
    @abstractmethod
    def submit(self, order: "Order") -> None:
        pass

    @abstractmethod
    def send_to_kitchen(self, order: "Order") -> None:
        pass

    @abstractmethod
    def prepare(self, order: "Order") -> None:
        pass

    @abstractmethod
    def mark_ready(self, order: "Order") -> None:
        pass

    @abstractmethod
    def get_status_name(self) -> str:
        pass