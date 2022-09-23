from abc import ABC, abstractmethod


class Disposable(ABC):
    @abstractmethod
    def dispose(self):
        pass

    def isDisposed(self):
        return False
