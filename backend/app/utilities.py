import calendar
from datetime import datetime

def monthEndDateValue(date):
    # Format = YYYY-MM-DD
    year = int(date[0:4])
    month = int(date[5:6])
    monthEndDate = calendar.monthrange(year, month)[1]
    return year, month, monthEndDate


def retEndDate(date):
    year, month, monthEndDate = monthEndDateValue(date)
    endDate = "-".join([str(year), str(month), str(monthEndDate)])
    return endDate