import calendar

def monthEndDay(date):
    # Format = YYYY-MM-DD
    year = int(date[0:4])
    month = int(date[5:6])
    monthEndDay = calendar.monthrange(year, month)[1]
    return year, month, monthEndDay


def endDate(date):
    year, month, monthEndDay = monthEndDay(date)
    endDate = "-".join([str(year), str(month), str(monthEndDay)])
    return endDate