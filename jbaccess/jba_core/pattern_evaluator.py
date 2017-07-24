import datetime

from typing import List


# - from_time - datetime.timedelta that represents from part of time interval
# - until_time - datetime.timedelta that represents until part of time interval
# - days_of_week - array that represents allowed weekdays at interval [1, 7]. 1 - monday, 7 - sunday.
#   Empty list means that all weekdays are allowed
# - days_of_month - array that represents allowed days of month at interval [1, 31]
#   Empty list means that all month days are allowed
# - months - array that represents allowed months at interval [1, 12]. 1 - January, 12 - December.
#   Empty list means that all months are allowed
def pattern_eval_date(eval_date: datetime.datetime, from_time: datetime.timedelta, until_time: datetime.timedelta,
                      days_of_week: List[int], days_of_month: List[int], months: List[int]) -> bool:
    if len(months) > 0 and eval_date.month not in months:
        return False
    if len(days_of_month) > 0 and eval_date.day not in days_of_month:
        return False
    if len(days_of_week) > 0 and (eval_date.weekday() + 1) not in days_of_week:
        return False
    from_date = datetime.datetime.combine(eval_date.date(), datetime.time.min) + from_time
    until_date = datetime.datetime.combine(eval_date.date(), datetime.time.min) + until_time
    if from_date > eval_date or until_date < eval_date:
        return False
    return True
