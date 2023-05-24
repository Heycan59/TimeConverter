from datetime import datetime, timezone, timedelta

class TimeConverter:
    def timelog():
        dt1 = datetime.utcnow().replace(tzinfo=timezone.utc)
        dt2 = dt1.astimezone(timezone(timedelta(hours=8)))
        now = dt2.strftime("%Y-%m-%d %H:%M:%S")
        return now