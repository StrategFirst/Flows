from urllib import request
from urllib import parse
import re
import json

class ytbSearchScrapper:

    def __init__(self , query: str):
        self.results = [
                {
                    'id' : d.get('videoId'),
                    #'thumbnail': d.get('thumbnail'),
                    'title': d.get('title').get('runs')[0].get('text'),
                    'length': d.get('lengthText').get('simpleText'),
                    'views': re.sub('\\?\\?\\??',' ',d.get('viewCountText').get('simpleText')),
                }
            for
                d
            in
                ytbSearchScrapper.get(query)
            if
                d != None
        ]

    def __str__(self):
        return "ytbSearchScrapper(\n"+('\n'.join(
            "\t %10s | %8s | %15s | %s "%(r.get('id'),r.get('length'),r.get('views'),r.get('title'))
            for r in self.results
        ))+"\n)"
        
    @staticmethod
    def get( query:str) -> any:
        return (
            ytbSearchScrapper.getInformation(
                ytbSearchScrapper.cleaningUp(
                    ytbSearchScrapper.extractInitialState(
                        ytbSearchScrapper.getPureHTML(
                            query
                        )
                    )
                )
            )
        )

    @staticmethod
    def getPureHTML( query :str ) -> str:
        URL = f"https://www.youtube.com/results?search_query={ parse.quote_plus( query ) }"
        RES = request.urlopen( URL ).read()
        return str(RES)

    @staticmethod
    def extractInitialState( HTML :str ) -> str:
        return re.search(
            'ytInitialData\s*=\s*([^;]*);',
            HTML
        ).groups()[0]

    @staticmethod
    def cleaningUp( JScode :str ) -> str:
        regexes = [ '\\\\\\\\"' , "\\\\'" , '\\\\x..' ]
        replacements = ['\\"',"'",'?']
        for regex,substitute in zip(regexes,replacements):
            JScode = re.sub( regex , substitute , JScode )
        return JScode

    @staticmethod
    def getInformation( JSON :str ) -> str:
        keys = ['contents','twoColumnSearchResultsRenderer','primaryContents','sectionListRenderer','contents']
        data = json.loads( JSON )
        for k in keys:
            data = data.get(k)
        data = data[0].get('itemSectionRenderer').get('contents')
        return [ v.get('videoRenderer') for v in data ]

