from PyQt5.QtCore import QThreadPool


class GlobalThreadPool(QThreadPool):
    def __new__(cls, *args):
        if not hasattr(cls, 'instance'):
            setattr(cls, 'instance', super().__new__(cls))
        return getattr(cls, 'instance')
