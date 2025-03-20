from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QDialog, QVBoxLayout, QLabel, QFormLayout, QPushButton
from windows.worker import Worker
from ds.etran_repository import EtranRepository
from windows.global_pool import GlobalThreadPool
from ds.schemes.GetInvoiceDetails import InvoiceDetailsResponse


class InvoiceDetailsDialog(QDialog):
    invoice_signed_signal = pyqtSignal()

    def __init__(self, invoice_id: str):
        super().__init__()
        self.setWindowTitle(f"Детали накладной {invoice_id}")
        self.resize(1920, 1080)
        layout = QVBoxLayout(self)
        self.pool = GlobalThreadPool()

        self.form_layout = QFormLayout()
        layout.addLayout(self.form_layout)

        self.loading_label = QLabel(
            "Загрузка данных, пожалуйста, подождите...", self)
        layout.addWidget(self.loading_label)

        close_button = QPushButton("Закрыть")
        close_button.clicked.connect(self.close)
        layout.addWidget(close_button)

        self.sign_button = QPushButton("🔏 Подписать накладную")
        self.sign_button.clicked.connect(self._sign_invoice)
        self.sign_button.setEnabled(False)
        layout.addWidget(self.sign_button)

        self.invoice_id = invoice_id
        self.display()

    def _sign_invoice(self):
        self.sign_button.setText("⌛ Подписываем...")
        self.sign_button.setEnabled(False)

        worker = Worker(
            lambda: EtranRepository().sign_invoice(self.invoice_id))
        worker.signals.result.connect(self._finish_signing)
        self.pool.start(worker)

    def _finish_signing(self, result):
        self.sign_button.setText("✅ Подписано")
        self.invoice_signed_signal.emit()

    def display(self) -> Worker:
        worker = Worker(
            EtranRepository().get_invoice_details,
            self.invoice_id
        )
        worker.signals.result.connect(self._display)
        self.pool.start(worker)

    def _display(self, data: InvoiceDetailsResponse):
        self.loading_label.hide()

        self.form_layout.addRow("Требуется ли подпись:",
                                QLabel(data.invNeedForECP_display))
        self.form_layout.addRow("Можно ли подписать:",
                                QLabel(data.invECPSign_display))

        self.form_layout.addRow("ID накладной:", QLabel(data.invoiceID))
        self.form_layout.addRow("№ накладной:", QLabel(data.invNumber))
        self.form_layout.addRow("Состояние:", QLabel(data.invoiceState))

        self.form_layout.addRow(
            "Дата создания документа:", QLabel(data.invDateCreate))
        self.form_layout.addRow(
            "Дата предъявления накладной:", QLabel(data.invDatePres))

        self.form_layout.addRow("Тип:", QLabel(data.invTypeName))
        self.form_layout.addRow("Отправитель:", QLabel(data.invSenderName))
        self.form_layout.addRow("Отправление:", QLabel(
            f"{data.invFromCountryName}, {data.invFromStationName}"))
        self.form_layout.addRow("Получатель:", QLabel(data.invRecipName))
        self.form_layout.addRow("Назначение:", QLabel(
            f"{data.invToCountryName}, {data.invToStationName}"))
        self.form_layout.addRow("Тип вагона:", QLabel(data.invPlanCarTypeName))
        self.form_layout.addRow("Принадлежность:", QLabel(
            data.invPlanCarOwnerTypeName))
        self.form_layout.addRow("Груз:", QLabel(
            data.invFreight.freightName if data.invFreight else '-'))
        self.form_layout.addRow("ГТД:", QLabel(data.freightGTDNumber or '-'))
        self.form_layout.addRow("Порт:", QLabel(data.invToPortName or '-'))

        self.sign_button.setEnabled(True)
