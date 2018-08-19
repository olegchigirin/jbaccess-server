from jba_ui.common.const import DAYS_OF_WEEK, MONTHS


def drop_squared_brackets(value: str):
    return value[1:-1]


def replace_days_of_week_for_names(value):
    for number, day in DAYS_OF_WEEK:
        value = value.replace(str(number), day)
    return value


def replace_months_for_names(value):
    for number, month in MONTHS:
        value = value.replace(str(number), month)
    return value
