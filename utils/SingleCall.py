from typing import Callable

import datetime
import time
import threading

class SingleCall:

    def __init__(
        self,

        function :Callable,
        delay :int, # seconds

    ):
        self.function = function
        self.delay = delay
        self.up = False
        self.argv = None

    def __call__(
        self,

        **kwargs
    ):        
        self.argv = kwargs
        if not self.up :
            threading.Timer( self.delay , self._doit_ ).start()
            self.up = True

    def _doit_( self ) -> None:
        self.function( **self.argv )
        self.up = False


            
