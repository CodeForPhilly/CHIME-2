# -*- coding: utf-8 -*-
"""Datetime and time series"""

import datetime as dt


def to_datetime(pattern: str, dt_format: str = "ISO-8601"):
    if dt_format == "ISO-8601":
        out = "%Y-%m-%d"
        return dt.datetime.strptime(pattern, out)
    else:
        return dt.datetime.strptime(pattern, str(dt_format))


class DatetimeArray(object):
    def __init__(self, arr=None, dt_format: str = "ISO-8601"):
        self.dates = [to_datetime(date, dt_format) for date in arr]

    def extend(self, n_days: int = 200):
        """Extend the index by ``n_days``.

        :param n_days: Number of days by which to extend the array.
        :type n_days: int
        """
        if not isinstance(n_days, int):
            arg_type = type(n_days)
            raise TypeError(
                f"'{arg_type}' invalid type for n_days. Must be of type int."
            )
        base = self.dates[-1]
        for day in range(1, n_days + 1):
            self.dates += [base + dt.timedelta(days=day)]
