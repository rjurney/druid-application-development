import datetime

def round_time(dt=None, roundTo=1):
    """Round a datetime object to any time laps in seconds
    dt : datetime.datetime object, default now.
    roundTo : Closest number of seconds to round to, default 1 second.
    Author: Thierry Husson 2012 - Use it as you want but don't blame me.
    """
    if dt == None : dt = datetime.datetime.now()
    seconds = (dt - dt.min).seconds
    # // is a floor division, not a comment on following line:
    rounding = (seconds+roundTo/2) // roundTo * roundTo
    return dt + datetime.timedelta(0,rounding-seconds,-dt.microsecond)

def prepare_intervals(duration):
    now = round_time(datetime.datetime.utcnow())
    now_iso = now.isoformat()
    ago = round_time(now - datetime.timedelta(seconds=duration))
    ago_iso = ago.isoformat()
    return [ago_iso, now_iso]

def prepend_anchor(counts, dt):
    # To give us an empty margin, we need a 0.0 stamped at the left-most time edge, 
    # and right at the start of our data
    if len(counts) > 0:
        anchor = [{"timestamp": dt + ".000Z", "result": {"count": 0.0}}]
        left_most = [{"timestamp": counts[0]['timestamp'], "result": {"count": 0.0}}]
        return anchor + left_most + counts
    else:
        return counts
