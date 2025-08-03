import time
from dataclasses import dataclass, field
from typing import ClassVar, Callable, Optional
from contextlib import ContextDecorator


class TimerError(BaseException):
    pass


@dataclass
class Timer(ContextDecorator):
    timers: ClassVar[dict[str, float]] = {}
    name: str | None = None
    text: str = "Elapsed time: {:0.4f} seconds"
    logger: Optional[Callable[[str], None]] = print
    _start_time: Optional[float] = field(default=None, init=False, repr=False)

    def __post_init__(self) -> None:
        "Add timer to dict of timers"
        if self.name:
            self.timers.setdefault(self.name, 0)

    def start(self) -> None:
        if self._start_time is not None:
            raise TimerError(f"Timer is running already")

        self._start_time = time.perf_counter()

    def stop(self) -> float:
        if self._start_time is None:
            raise TimerError(
                f"Timer is not running")

        elapsed_time = time.perf_counter() - self._start_time
        self._start_time = None

        if self.logger:
            self.logger(self.text.format(elapsed_time))

        if self.name:
            self.timers[self.name] += elapsed_time

        return elapsed_time

    def __enter__(self):
        self.start()
        return self

    def __exit__(self, *exc_info):
        self.stop()
