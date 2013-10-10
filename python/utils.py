import datetime

def round_time(dt=None, roundTo=1):
    """Round a datetime object to any time laps in seconds
    dt : datetime.datetime object, default now.
    roundTo : Closest number of seconds to round to, default 1 minute.
    Author: Thierry Husson 2012 - Use it as you want but don't blame me.
    """
    if dt == None : dt = datetime.datetime.now()
    seconds = (dt - dt.min).seconds
    # // is a floor division, not a comment on following line:
    rounding = (seconds+roundTo/2) // roundTo * roundTo
    return dt + datetime.timedelta(0,rounding-seconds,-dt.microsecond)

def prepare_intervals():
    now = round_time(datetime.datetime.utcnow())
    now_iso = now.isoformat()
    ago = round_time(now - datetime.timedelta(seconds=10))
    ago_iso = ago.isoformat()
    interval = [ago_iso + "Z" + "/" + now_iso + "Z"]
    return interval
