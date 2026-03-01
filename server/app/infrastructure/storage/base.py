from abc import ABC, abstractmethod

class BaseStorage(ABC):

    @abstractmethod
    def save(self, file, filename: str) -> str:
        pass