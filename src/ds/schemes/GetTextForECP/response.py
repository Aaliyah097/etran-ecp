from pydantic import BaseModel


class GetTextForECPResponse(BaseModel):
    userID: int
    userFIO: str
    DocID: int
    textBinary: str
