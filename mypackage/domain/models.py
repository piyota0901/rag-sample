# {
#     "name":"SaferCodes",
#     "images":"https:\/\/safer.codes\/img\/brand\/logo-icon.png",
#     "alt":"SaferCodes Logo QR codes generator system forms for COVID-19",
#     "description":"QR codes systems for COVID-19.\nSimple tools for bars restaurants, offices, and other small proximity businesses.",
#     "link":"https:\/\/safer.codes",
#     "city":"Chicago"
# }

class Startup:
    def __init__(
        self, 
        id: str, 
        score: float,
        name: str, 
        alt: str, 
        description: str, 
        link: str, 
        city: str, 
        images: str, 
        *args, 
        **kwargs
    ):
        self.__id = id
        self.__score = score
        self.__name = name
        self.__alt = alt
        self.__description = description
        self.__link = link
        self.__city = city
        self.__images = images
    
    @property
    def id(self):
        return self.__id
    
    @property
    def score(self):
        return self.__score
    
    @property
    def name(self):
        return self.__name
    
    @property
    def alt(self):
        return self.__alt
    
    @property
    def description(self):
        return self.__description
    
    @property
    def link(self):
        return self.__link
    
    @property
    def city(self):
        return self.__city
    
    @property
    def images(self):
        return self.__images