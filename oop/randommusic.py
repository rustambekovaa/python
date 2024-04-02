import random
class Albom:
    def __init__(self,artist,albom,list):
        self.artist = artist
        self.albom = albom
        self.list = list
        
    def info(self):
        # k = random.choice(self.list)  
        print(f'artist: {self.artist} \n albom: {self.albom} \n list: {random.choice(self.list)}')
        
        
alm=Albom("Adele"," Sommer time is saddnes",["love in The dark  ","Hello","Oh my God ","Some one like you "])        
alm.info()