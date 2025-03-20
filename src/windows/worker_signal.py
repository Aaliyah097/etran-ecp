from PyQt5.QtCore import QObject, pyqtSignal
import traceback
import sys


class WorkerSignals(QObject):
    finished = pyqtSignal()
    error = pyqtSignal(tuple)
    result = pyqtSignal(object)
