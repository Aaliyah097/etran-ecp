from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QSizePolicy, QVBoxLayout, QRadioButton, QDialog, QLabel, QFormLayout, QPushButton
from windows.worker import Worker
from ds.etran_repository import EtranRepository
from windows.global_pool import GlobalThreadPool
from cryptopro.list_certificates import list_certificates
from cryptopro.get_csp_version import get_csp_version
from global_state import GLOBAL_STATE


class SelectCertDialog(QDialog):
    invoice_signed_signal = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.setWindowTitle(f"Версия КриптоПРО {get_csp_version()}")
        self.resize(1920, 1080)
        layout = QVBoxLayout(self)
        self.pool = GlobalThreadPool()

        self.form_layout = QFormLayout()
        layout.addLayout(self.form_layout)

        self.loading_label = QLabel(
            "Загрузка данных, пожалуйста, подождите...", self)
        layout.addWidget(self.loading_label)

        close_button = QPushButton("Выбрать сертификат")
        close_button.clicked.connect(self.show_selection)
        layout.addWidget(close_button)

        self.radio_buttons = []
        self.display()

    def display(self) -> Worker:
        self.loading_label.hide()

        certs = list_certificates()

        self.radio_buttons.clear()
        for key, value in certs.items():
            radio = QRadioButton(value)
            setattr(radio, 'cert_number', key)
            radio.setMaximumSize(1920, 1080)
            self.form_layout.addWidget(radio)
            self.radio_buttons.append(radio)

    def show_selection(self):
        for radio in self.radio_buttons:
            if radio.isChecked():
                GLOBAL_STATE['cert_number'] = getattr(radio, 'cert_number')
                self.close()
