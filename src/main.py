from datetime import *
from dateutil.rrule import *

next_date = rrule(YEARLY, count=1, dtstart=datetime.now(),
                  bymonthday=13, byweekday=FR)[0]
print("Next 13th Friday is %s" % (next_date.date()))
