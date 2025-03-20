from datetime import datetime
from pydantic import BaseModel
from ds.schemes.etran_dt import etrandatetime


class DocState(BaseModel):
    StateId: int
    StateName: str


class DocType(BaseModel):
    DocTypeId: int
    DocTypeName: str


class Document(BaseModel):
    DOC_ID: int
    Last_Date: etrandatetime
    DocDescription: str
    DocState: DocState
    DocType: DocType


class ECPDocType(BaseModel):
    ECPDocTypeID: int
    ECPDocTypeName: str | None = None


class ECPWaitDocument(BaseModel):
    Document: Document
    ECPDate: etrandatetime
    ECPDocType: ECPDocType


class UnsignedInvoicesResponse(BaseModel):
    OperId: int
    OperDate: etrandatetime
    ECPWaitDocument: list[ECPWaitDocument]
