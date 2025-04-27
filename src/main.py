from datetime import datetime
from dateutil.rrule import *


def next_13th_friday() -> datetime:
    return rrule(YEARLY, count=1, dtstart=datetime.now(),
                 bymonthday=13, byweekday=FR)[0]


if __name__ == '__main__':
    formatted = next_13th_friday().strftime("%x")
    print(f"Next 13th Friday is {formatted}")
