import datetime
from _typeshed import Incomplete
from collections.abc import Iterable
from typing import Any
from typing_extensions import TypeAlias

from ._common import weekday as weekdaybase

YEARLY: int
MONTHLY: int
WEEKLY: int
DAILY: int
HOURLY: int
MINUTELY: int
SECONDLY: int

class weekday(weekdaybase): ...

weekdays: tuple[weekday, weekday, weekday, weekday, weekday, weekday, weekday]
MO: weekday
TU: weekday
WE: weekday
TH: weekday
FR: weekday
SA: weekday
SU: weekday

class rrulebase:
    def __init__(self, cache: bool = ...) -> None: ...
    def __iter__(self): ...
    def __getitem__(self, item): ...
    def __contains__(self, item): ...
    def count(self): ...
    def before(self, dt, inc: bool = ...): ...
    def after(self, dt, inc: bool = ...): ...
    def xafter(self, dt, count: Incomplete | None = ..., inc: bool = ...): ...
    def between(self, after, before, inc: bool = ..., count: int = ...): ...

class rrule(rrulebase):
    def __init__(
        self,
        freq,
        dtstart: datetime.date | None = ...,
        interval: int = ...,
        wkst: weekday | int | None = ...,
        count: int | None = ...,
        until: datetime.date | int | None = ...,
        bysetpos: int | Iterable[int] | None = ...,
        bymonth: int | Iterable[int] | None = ...,
        bymonthday: int | Iterable[int] | None = ...,
        byyearday: int | Iterable[int] | None = ...,
        byeaster: int | Iterable[int] | None = ...,
        byweekno: int | Iterable[int] | None = ...,
        byweekday: int | weekday | Iterable[int] | Iterable[weekday] | None = ...,
        byhour: int | Iterable[int] | None = ...,
        byminute: int | Iterable[int] | None = ...,
        bysecond: int | Iterable[int] | None = ...,
        cache: bool = ...,
    ) -> None: ...
    def replace(self, **kwargs): ...

class _iterinfo:
    rrule: Any = ...
    def __init__(self, rrule) -> None: ...
    yearlen: int = ...
    nextyearlen: int = ...
    yearordinal: int = ...
    yearweekday: int = ...
    mmask: Any = ...
    mdaymask: Any = ...
    nmdaymask: Any = ...
    wdaymask: Any = ...
    mrange: Any = ...
    wnomask: Any = ...
    nwdaymask: Any = ...
    eastermask: Any = ...
    lastyear: int = ...
    lastmonth: int = ...
    def rebuild(self, year, month): ...
    def ydayset(self, year, month, day): ...
    def mdayset(self, year, month, day): ...
    def wdayset(self, year, month, day): ...
    def ddayset(self, year, month, day): ...
    def htimeset(self, hour, minute, second): ...
    def mtimeset(self, hour, minute, second): ...
    def stimeset(self, hour, minute, second): ...

_RRule: TypeAlias = rrule

class rruleset(rrulebase):
    class _genitem:
        dt: Any = ...
        genlist: Any = ...
        gen: Any = ...
        def __init__(self, genlist, gen) -> None: ...
        def __next__(self): ...
        next: Any = ...
        def __lt__(self, other): ...
        def __gt__(self, other): ...
        def __eq__(self, other): ...
        def __ne__(self, other): ...

    def __init__(self, cache: bool = ...) -> None: ...
    def rrule(self, rrule: _RRule): ...
    def rdate(self, rdate): ...
    def exrule(self, exrule): ...
    def exdate(self, exdate): ...

class _rrulestr:
    def __call__(self, s, **kwargs) -> rrule | rruleset: ...

rrulestr: _rrulestr
