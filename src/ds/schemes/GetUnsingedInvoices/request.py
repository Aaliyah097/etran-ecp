import pytz
from typing import Tuple
from datetime import date, datetime, time


def UnsignedInvoicesRequest(date_begin: date, date_end: date) -> Tuple[str, str]:
    timezone = pytz.timezone('Europe/Moscow')
    date_begin = datetime.combine(date_begin, time.min, timezone)
    date_end = datetime.combine(date_end, time.max, timezone)

    return (
        """<ECPWaitDocStatus>
            <fromDate>%s</fromDate>
            <toDate>%s</toDate>
        </ECPWaitDocStatus>""" % (
            date_begin.strftime(r"%d.%m.%Y %H:%M:%S"),
            date_end.strftime(r"%d.%m.%Y %H:%M:%S")
        ),
        'ECPWaitDocStatusReplay'
    )
