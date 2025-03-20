from datetime import date
from PyQt5.QtWidgets import (
    QMainWindow,
    QPushButton,
    QWidget,
    QVBoxLayout,
)
from windows.widgets.unsigned_invoices_table import UnsignedInvoicesTable
from windows.widgets.select_cert_dialog import SelectCertDialog


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Подписание накладных в ЭТРАН")
        self.resize(1920, 1080)

        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)

        table = UnsignedInvoicesTable()
        layout.addWidget(table)
        table.display()

        update_button = QPushButton("Обновить")
        update_button.clicked.connect(table.display)
        layout.addWidget(update_button)

        select_cert_dialog = SelectCertDialog()
        select_cert_dialog.exec_()
