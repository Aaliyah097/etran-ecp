from typing import Dict
import win32com.client


def list_certificates() -> Dict[int, str]:
    store = win32com.client.Dispatch("CAdESCOM.Store")
    store.Open(2, "CA", 0)
    return {
        (idx+1): f"Сертификат: {cert.SubjectName}\n(Выдан: {cert.IssuerName})"
        for idx, cert in enumerate(store.Certificates)
    }
