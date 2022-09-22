from abc import ABC, abstractmethod
from src.pArc.utils import synchronized, disposable


class Application(ABC, disposable.Disposable):
    @abstractmethod
    def getListeners(self):
        pass

    @synchronized
    def addListener(self, listener):
        self.getListeners().append(listener)

    @synchronized
    def removeListener(self, listener):
        self.getListeners().remove(listener)
