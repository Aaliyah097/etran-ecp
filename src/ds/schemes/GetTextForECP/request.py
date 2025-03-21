from typing import Tuple


def GetTextForECPRequest(
    invoice_id: str,
) -> Tuple[str, str]:
    return (
        f"""<getTextForECP>
			<docID value="{invoice_id}"/>
            <useBinary/>
		</getTextForECP>""",
        "getTextForECPReply"
    )
