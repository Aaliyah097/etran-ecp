def GetTextForECPRequest(
    invoice_id: str,
) -> tuple[str, str]:
    return (
        f"""<getTextForECP>
			<docID value="{invoice_id}"/>
            <useBinary/>
		</getTextForECP>""",
        "getTextForECPReply"
    )
