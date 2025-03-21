from typing import Tuple


def SetECPRequest(invoice_id: int, data: str, sign: str) -> Tuple[str, str]:
    return (
        """<setECP>
            <docID value="%s"/>
            <textBinary value="%s"/>
            <ecp value="%s"/>
            <version value="5"/>
            <useBinary/>
        </setECP>""" % (
            invoice_id,
            data,
            sign
        ),
        'setECPReply'
    )
