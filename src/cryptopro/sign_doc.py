import win32com.client
import base64
from global_state import GLOBAL_STATE


def sign_doc(binary_data):
    if not GLOBAL_STATE['cert_number']:
        raise KeyError("Не выбран сертификат")

    store = win32com.client.Dispatch("CAdESCOM.Store")
    store.Open(2, "My", 0)
    cert = store.Certificates.Item(GLOBAL_STATE['cert_number'])

    signedData = win32com.client.Dispatch("CAdESCOM.CadesSignedData")
    # signedData.ContentEncoding = 1
    signedData.Content = binary_data

    signer = win32com.client.Dispatch("CAdESCOM.CPSigner")
    signer.Certificate = cert

    # False = присоединенная подпись
    signature = signedData.SignCades(signer, 1, True)

    return signature
