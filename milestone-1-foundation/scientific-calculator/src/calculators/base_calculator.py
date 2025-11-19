from abc import ABC, abstractmethod


class BaseCalculator(ABC):
    """Abstract base class for calculators."""
    @abstractmethod
    def add(self, a: float, b: float) -> float:
        pass

    @abstractmethod
    def subtract(self, a: float, b: float) -> float:
        pass

    @abstractmethod
    def multiply(self, a: float, b: float) -> float:
        pass

    @abstractmethod
    def divide(self, a: float, b: float) -> float:
        pass
