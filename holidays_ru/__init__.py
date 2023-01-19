from datetime import date

__version__ = "0.1"

MOVED_HOLIDAYS = [
    date(2020, 2, 24), date(2020, 3, 9), date(2020, 5, 4), date(2020, 5, 5), date(2020, 5, 11),
    # date(2022, 12, 11),
]

WORK_WEEKENDS = []

WEEKENDS = "Выходной"
MOVED_HOLIDAY = "Передвинутый выходной"


def is_holiday(d: date) -> str:
    # New Year's Day
    if d.month == 1 and d.day in (1, 2, 3, 4, 5, 6, 8):
        return "Новый год"
    if d.month == 1 and d.day == 7:
        return "Православное Рождество"
    # Man Day
    if d.month == 2 and d.day == 23:
        return "День защитника отечества"
    # Women's Day
    if d.month == 3 and d.day == 8:
        return "День женщин"
    # Labour Day
    if d.month == 5 and d.day == 1:
        return "Праздник Весны и Труда"
    # Victory Day
    if d.month == 5 and d.day == 9:
        return "День Победы"
    # Russia's Day
    if d.month == 6 and d.day == 12:
        return "День России"
    if d.year >= 2005:
        # Unity Day
        if d.month == 11 and d.day == 4:
            return "День народного единства"
    else:
        # October Revolution Day
        if d.month == 11 and d.day == 7:
            return "День Октябрьской революции"
    if d in MOVED_HOLIDAYS:
        return MOVED_HOLIDAY
    if d in WORK_WEEKENDS:
        return ''
    if d.weekday() in (6, 7):
        return WEEKENDS
    return ''


def check_holiday(d: date, with_weekends: bool = True) -> bool:
    r = is_holiday(d)
    if not with_weekends and r == WEEKENDS:
        return False
    return bool(r)
