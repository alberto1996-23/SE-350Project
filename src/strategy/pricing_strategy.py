from abc import ABC, abstractmethod
from ../order import Order

class PricingStrategy:
    def calculate_total(order: Order) -> double:
        
