from abc import ABC, abstractmethod


class ApplicationListener(ABC):
    def __init__(self):
        pass

    def init(self):
        pass

    def resize(self, width: int, height: int):
        pass

    def update(self):
        pass

    def pause(self):
        pass

    def resume(self):
        pass

    def dispose(self):
        pass

    def exit(self):
        pass

    def file_dropped(self, file):
        pass
