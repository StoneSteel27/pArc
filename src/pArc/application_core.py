from abc import abstractmethod
from src.pArc.application_listener import ApplicationListener


class ApplicationCore(ApplicationListener):
    _modules = []

    def __init__(self):
        super().__init__()

    @abstractmethod
    def setup(self):
        pass

    def init(self):
        self.setup()
        for listener in ApplicationCore._modules:
            listener.init()

    def add(self, module: ApplicationListener):
        ApplicationCore._modules.append(module)

    def resize(self, width: int, height: int):
        for listener in ApplicationCore._modules:
            listener.resize(width, height)

    def update(self):
        for listener in ApplicationCore._modules:
            listener.update()

    def pause(self):
        for listener in ApplicationCore._modules:
            listener.pause()

    def resume(self):
        for listener in ApplicationCore._modules:
            listener.resume()

    def dispose(self):
        for listener in ApplicationCore._modules:
            listener.dispose()

    def file_dropped(self, file):
        for listener in ApplicationCore._modules:
            listener.fileDropped(file)
