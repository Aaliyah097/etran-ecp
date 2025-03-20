import win32com.client


def get_csp_version() -> str:
    return win32com.client.Dispatch("CAdESCOM.About").Version
