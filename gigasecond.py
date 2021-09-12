import datetime

def gigasecond(momento):
    gigasec = datetime.timedelta(seconds=1000000000)
    gigasecxgiorno = gigasec + momento
    return gigasecxgiorno