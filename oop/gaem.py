class Players_Char:
    def __init__(self,name,health):
        self.person_name=name
        self.health_count= health
    
    def atack(self,atakker):
        print(self.person_name,"vs",atakker.person_name)
        print(f"Health{self.health_count}- Ataker{atakker.health_count}")
        if self.health_count < atakker.health_count:
            print(f"{self.person_name} проиграл")
        else:
            print(f"Ваш противник {atakker.person_name} проиграл")       

tom = Players_Char("Tom",100)
andrew = Players_Char("Andrew",110) 
andrew.atack(tom)           


