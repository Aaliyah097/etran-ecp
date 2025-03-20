from PyQt5.QtWidgets import QTableWidget, QHeaderView, QTableWidgetItem, QAbstractItemView
from windows.worker import Worker
from ds.etran_repository import EtranRepository, UnsignedInvoicesResponse
from windows.global_pool import GlobalThreadPool
from windows.widgets.invoice_details_dialog import InvoiceDetailsDialog


class UnsignedInvoicesTable(QTableWidget):
    def __init__(self):
        super().__init__()
        self.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.pool = GlobalThreadPool()
        self.cellDoubleClicked.connect(self.row_details)
        self.setEditTriggers(QAbstractItemView.NoEditTriggers)

    def display(self) -> Worker:
        worker = Worker(EtranRepository().get_unsigned_invoices)
        worker.signals.result.connect(self._display)
        self.pool.start(worker)

    def row_details(self, row: int, _: int):
        dialog = InvoiceDetailsDialog(self.item(row, 0).text())
        dialog.invoice_signed_signal.connect(self.display)
        dialog.exec_()

    def _display(self, data: UnsignedInvoicesResponse) -> None:
        docs = data.ECPWaitDocument

        headers = [
            "Идентификатор",
            "Дата",
            "Описание",
            "Статус",
            "Тип",
            "Дата ЭЦП",
            "Тип ЭЦП"
        ]

        self.setRowCount(len(docs))
        self.setColumnCount(len(headers))
        self.setHorizontalHeaderLabels(headers)

        for row_idx, row in enumerate(docs):
            doc = row.Document

            self.setItem(row_idx, 0, QTableWidgetItem(str(doc.DOC_ID)))
            self.setItem(row_idx, 1, QTableWidgetItem(str(doc.Last_Date)))
            self.setItem(row_idx, 2, QTableWidgetItem(str(doc.DocDescription)))
            self.setItem(row_idx, 3, QTableWidgetItem(
                str(doc.DocState.StateName)))
            self.setItem(row_idx, 4, QTableWidgetItem(
                str(doc.DocType.DocTypeName)))
            self.setItem(row_idx, 5, QTableWidgetItem(str(row.ECPDate)))
            self.setItem(row_idx, 6, QTableWidgetItem(
                str(row.ECPDocType.ECPDocTypeName)))
