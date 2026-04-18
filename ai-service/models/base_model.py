from abc import ABC, abstractmethod


class BaseKTModel(ABC):
    @abstractmethod
    def build(self, **kwargs):
        pass

    @abstractmethod
    def predict(self, input_data):
        pass
