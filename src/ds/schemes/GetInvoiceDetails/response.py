from typing import List, Optional, Union
from pydantic import BaseModel


class Freight(BaseModel):
    freightCode: Optional[str] = None
    freightName: Optional[str] = None
    freightWeight: Optional[str] = None
    freightRealWeight: Optional[str] = None
    freightDangerSignID: Optional[str] = None
    freightDangerSignName: Optional[str] = None
    freightID: Optional[str] = None


class InvoiceDetailsResponse(BaseModel):
    invoiceID: Optional[str] = None
    invUNP: Optional[str] = None
    invoiceStateID: Optional[str] = None
    invoiceState: Optional[str] = None
    invLastOper: Optional[str] = None
    invNeedForECP: Optional[str] = None
    invECPSign: Optional[str] = None
    invDateCreate: Optional[str] = None
    invDatePres: Optional[str] = None
    invTypeID: Optional[str] = None
    invTypeName: Optional[str] = None
    invBlankTypeID: Optional[str] = None
    invBlankType: Optional[str] = None
    invBlankTypeName: Optional[str] = None
    invSenderID: Optional[str] = None
    invSenderOKPO: Optional[str] = None
    invSenderName: Optional[str] = None
    invSenderAddressID: Optional[str] = None
    invSenderAddress: Optional[str] = None
    invSenderTGNL: Optional[str] = None
    invFromCountryCode: Optional[str] = None
    invFromCountryName: Optional[str] = None
    invFromStationCode: Optional[str] = None
    invFromStationName: Optional[str] = None
    invRecipID: Optional[str] = None
    invRecipOKPO: Optional[str] = None
    invRecipName: Optional[str] = None
    invRecipAddressID: Optional[str] = None
    invRecipAddress: Optional[str] = None
    invRecipTGNL: Optional[str] = None
    invToCountryCode: Optional[str] = None
    invToCountryName: Optional[str] = None
    invToStationCode: Optional[str] = None
    invToStationName: Optional[str] = None
    invSendSpeedID: Optional[str] = None
    invSendSpeedName: Optional[str] = None
    invSendKindID: Optional[str] = None
    invSendKindName: Optional[str] = None
    invPayPlaceID: Optional[str] = None
    invPayPlaceName: Optional[str] = None
    invPayFormID: Optional[str] = None
    invPayFormName: Optional[str] = None
    invPlanCarTypeID: Optional[str] = None
    invPlanCarTypeCode: Optional[str] = None
    invPlanCarTypeName: Optional[str] = None
    invPlanCarCount: Optional[str] = None
    invPlanCarOwnerTypeID: Optional[str] = None
    invPlanCarOwnerTypeName: Optional[str] = None
    invPlanContOwnerTypeID: Optional[str] = None
    invPlanContOwnerTypeName: Optional[str] = None
    invLoadTypeID: Optional[str] = None
    invLoadTypeName: Optional[str] = None
    invAnnounceValue: Optional[str] = None
    invAVCurrencyID: Optional[str] = None
    invLoadAssetsID: Optional[str] = None
    invLoadAssetsName: Optional[str] = None
    invDispKindID: Optional[str] = None
    invRespPerson: Optional[str] = None
    invPayerCode: Optional[str] = None
    invPayerId: Optional[str] = None
    invPayerName: Optional[str] = None
    invLoadClaim_ID: Optional[str] = None
    invLoadClaim_Number: Optional[str] = None
    invCheckDepID: Optional[str] = None
    invCheckDepName: Optional[str] = None
    invDateLoad: Optional[str] = None
    invDateExpire: Optional[str] = None
    invNumber: Optional[str] = None
    invSignRouteNumCirc: Optional[str] = None
    invFreight: Union[Freight, None] = None
    invFormPPSign: Optional[str] = None
    invTranspPurposeID: Optional[str] = None
    freightGTDNumber: Union[str, None] = None
    invToPortName: Union[str, None] = None

    @property
    def invNeedForECP_display(self) -> str:
        if self.invNeedForECP is None:
            return "?"

        if int(self.invNeedForECP) == -2:
            return "Признак оформления документа по технологии с использованием ЭП не вычислен"
        if int(self.invNeedForECP) == -1:
            return "Документ оформлен не по технологии с использованием ЭП"
        if int(self.invNeedForECP) == 0:
            return "ЭП не ожидается"
        if int(self.invNeedForECP) == 1:
            return "ЭП надо, но не от организации пользователя"
        if int(self.invNeedForECP) == 2:
            return "ЭП от организации пользователя"
        if int(self.invNeedForECP) == 3:
            return "ЭП от организации пользователя, но ТаймАут просрочен"
        if int(self.invNeedForECP) == 4:
            return "ЭП от организации пользователя и откатывать нельзя"

        return "Неизвестно"

    @property
    def invECPSign_display(self) -> str:
        if self.invECPSign is None:
            return "?"

        if int(self.invECPSign) == 0:
            return "не подписывается ЭП"
        if int(self.invECPSign) == 1:
            return "подписывается"
