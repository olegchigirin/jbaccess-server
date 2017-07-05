import datetime

from typing import List


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
