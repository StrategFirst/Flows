import customtkinter
from typing import Callable
class SizeHandler:

    _width = 0
    _height = 0
    _subscribed = []

    @staticmethod
    def setSize(app, width :int,height :int) -> None:
        app.geometry(f"{width}x{height}")
        SizeHandler._width = width
        SizeHandler._height = height
        for f in SizeHandler._subscribed:
            f()


    @staticmethod
    def handler(event) -> None:
        if (SizeHandler._width != event.width) or (SizeHandler._height != event.height):
            SizeHandler._width = event.width
            SizeHandler._height = event.height
            for f in SizeHandler._subscribed:
                f()

    @staticmethod
    def subscribe(f :Callable) -> None:
        SizeHandler._subscribed.append( f )


    @staticmethod
    def get_totalWidth() -> int:
        return SizeHandler._width
    @staticmethod
    def get_totalHeight() -> int:
        return SizeHandler._height
        

    @staticmethod
    def get_sidebarWidth() -> int:
        return 100
    @staticmethod
    def get_sidebarHeight() -> int:
        return SizeHandler._height


    @staticmethod
    def get_playerWidth() -> int:
        return SizeHandler._width - SizeHandler.get_sidebarWidth()
    @staticmethod
    def get_playerHeight() -> int:
        return 150


    @staticmethod
    def get_mainWidth() -> int:
        return SizeHandler._width - SizeHandler.get_sidebarWidth()
    @staticmethod
    def get_mainHeight() -> int:
        return SizeHandler._height - SizeHandler.get_playerHeight()