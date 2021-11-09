from abc import ABC , abstractmethod
import inspect
class Band():
    instances=[]

    def __init__(self,name,members):
        self.name=name
        self.members=members
        Band.instances.append(self)
        
    @classmethod
    def to_list(cls):
        return cls.instances

    def play_solos(self):
        solos=[]
        for i in self.members:
           solos += [i.play_solo()]
        return solos  
        # if Guitarist(self):
        #     return Guitarist.play_solo
        # if Bassist(self):
        #     return Bassist.play_solo
        # if Drummer(self):
        #     return Drummer.play_solo 
    
    def __str__(self):
        pass
    
    def __repr__(self):
        return f"'{self.name}'"
        
class Musician():
    instruments = []
    def __init__(self):
        
        @abstractmethod
        def get_instrument(self):
            Musician.instruments += [Guitarist.get_instrument(self)] + [Bassist.get_instrument(self)] + [Drummer.get_instrument(self)] 
            return Musician.instruments

        @abstractmethod
        def play_solo(self):
            if Guitarist(self):
                return Guitarist.play_solo
            if Bassist(self):
                return Bassist.play_solo
            if Drummer(self):
                return Drummer.play_solo

class Guitarist(Musician):

    def __init__(self, name):
        self.name=name

    def get_instrument(self):
        return "guitar"
    
    def play_solo(self):
        return "face melting guitar solo"

    def __str__(self):
        return f"My name is {self.name} and I play {Guitarist.get_instrument(self)}"

    def __repr__(self):
        return f"Guitarist instance. Name = {self.name}"

class Bassist(Musician):

    def __init__(self, name):
        self.name=name

    def get_instrument(self):
        return "bass"

    def play_solo(self):
        return "bom bom buh bom"

    def __str__(self):
        return f"My name is {self.name} and I play {Bassist.get_instrument(self)}"
        
    def __repr__(self):
        return f"Bassist instance. Name = {self.name}"

class Drummer(Musician):

    def __init__(self, name):
        self.name=name

    def get_instrument(self):
        return "drums"

    def play_solo(self):
        return "rattle boom crash"

    def __str__(self):
        return f"My name is {self.name} and I play {Drummer.get_instrument(self)}"
        
    def __repr__(self):
        return f"Drummer instance. Name = {self.name}"