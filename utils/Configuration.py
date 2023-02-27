import typing
import json

class Config:

    _instance_ = None

    @staticmethod
    def _load_():
        with open('config.json' , 'r') as config_file:
            return json.loads(config_file.read())

    @staticmethod
    def factory() -> 'Config':
        if Config._instance_ == None:
            Config._instance_ = Config()
        return Config._instance_

    def __init__( self ):
        self.data = self._load_()

    def __call__( self , args : typing.Union[typing.List[str],str] ):
        if type( args ) == str:
            args = [args] 
        search = self._instance_.data
        for arg in args:
            if arg not in search:
                raise KeyError
            search = search[arg]
        else:
            return search

    @staticmethod
    def get( args : typing.Union[typing.List[str],str] ):
        return Config.factory() ( args )

    @staticmethod
    def set( args : typing.Union[typing.List[str],str] , value : any , save = False ):

        if type( args ) == str:
            args = [args]

        i = Config.factory()
        k = i.data

        for arg in args[:-1]:
            if arg not in k:
                raise KeyError
            k = k[arg]
        else:
            k[args[-1]] = value

            if save:
                with open('config.json', 'w') as config_file:
                    json.dump( i.data , config_file )

            

        