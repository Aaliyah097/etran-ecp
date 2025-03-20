from datetime import date
import base64
from ds.etran_client import EtranClient, client_session
from ds.schemes.GetUnsingedInvoices import UnsignedInvoicesRequest, UnsignedInvoicesResponse
from ds.schemes.GetInvoiceDetails import InvoiceDetailsRequest, InvoiceDetailsResponse
from ds.schemes.GetTextForECP import GetTextForECPRequest, GetTextForECPResponse
from ds.schemes.SetECP import SetECPRequest
from cryptopro.sign_doc import sign_doc


class EtranRepository:
    def get_unsigned_invoices(self) -> UnsignedInvoicesResponse:
        print("Запрошены неподписанные накладные")
        with client_session() as session:
            return EtranClient().request(
                session,
                *(UnsignedInvoicesRequest(date.today(), date.today())),
                UnsignedInvoicesResponse
            )

    def get_invoice_details(self, invoice_id: int) -> InvoiceDetailsResponse:
        print("Запрошены детали накладной")
        with client_session() as session:
            return EtranClient().request(
                session,
                *InvoiceDetailsRequest(invoice_id=invoice_id,
                                       invoice_number=None),
                InvoiceDetailsResponse
            )

    def sign_invoice(self, invoice_id: int):
        base64_text = self.get_invoice_text_for_ecp(invoice_id).textBinary
        binary_data = base64.b64decode(base64_text)
        binary_signature = sign_doc(binary_data)

        with client_session() as session:
            EtranClient().request(
                session,
                *SetECPRequest(
                    invoice_id,
                    base64_text,
                    binary_signature
                ),
                None
            )

    def get_invoice_text_for_ecp(self, invoice_id: int) -> GetTextForECPResponse:
        print("Запрошено текстовое представление накладной для подпсиания")
        with client_session() as session:
            return EtranClient().request(
                session,
                *GetTextForECPRequest(invoice_id),
                GetTextForECPResponse
            )
