import logging
import re


class LogFilter(logging.Filter):
    def __init__(self, msg_pattern: str, name: str | None = None) -> None:
        if name:
            super().__init__(name)
        else:
            super().__init__()
        self._msg_pattern = msg_pattern

    def filter(self, record: logging.LogRecord) -> bool:
        return re.match(self._msg_pattern, record.getMessage()) is None
