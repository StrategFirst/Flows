from typing import Callable

import datetime
import time

class CallSingle:

    def _getUnixTimestamp_() -> int:
        return (time.mktime(date_time.timetuple()))

    def __init__(
        self,

        function :Callable,
        delay :int, # seconds

        now=False :bool,
    ):
        self.function = function
        self.timestamp = (self._getUnixTimestamp_() + delay ) if now else 0
        self.delay = delay

    def __call__(
        self,

        **kwargs
    ):
        now = self._getUnixTimestamp_()
        if self.timestamp < now :
            self.function(**kwargs)
            self.timestamp = now + self.delay

            
