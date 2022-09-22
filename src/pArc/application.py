from abc import ABC, abstractmethod
from pArc.utils.synchronized import synchronized
from pArc.utils.disposable import Disposable


class Application(ABC, Disposable):
    @abstractmethod
    def getListeners(self):
        pass

    @synchronized
    def addListener(self, listener):
        self.getListeners().append(listener)

    @synchronized
    def removeListener(self, listener):
        self.getListeners().remove(listener)
