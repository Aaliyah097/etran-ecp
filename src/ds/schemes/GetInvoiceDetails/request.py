def InvoiceDetailsRequest(
    invoice_id: str | None,
    invoice_number: str | None
) -> tuple[str, str]:
    if not invoice_id and not invoice_number:
        raise ValueError("Ожидлся ИД или номер накладной")

    if invoice_number:
        query = f"""<invNumber value="{invoice_number}"/>"""
    else:
        query = f"""<invoiceID value="{invoice_id}"/>"""

    return (
        f"""<getInvoice>
			{query}
			<usePay/>
		</getInvoice>""",
        "getInvoiceReply"
    )
