class Spaceship:
    __race = ''
    __typeOfCraft = ''
    __hyperDrive = ''
    __crew = ''

    def __init__(self, race:str, typeOfCraft:str, hyperDrive:bool, crew:int):
        self.__race = race
        self.__typeOfCraft = typeOfCraft
        self.__hyperDrive = hyperDrive 
        self.__crew = crew 
    
    def getRace(self)->str:
        return self.__race
            
    def getTypeOfCraft(self)->str:
        return self.__typeOfCraft

    def getHyperDrive(self)->bool:
        return self.__hyperDrive

    def getCrew(self)->int:
        return self.__crew
    
    def __str__(self):
        s='Spacefahring race: {} Type of craft: {} Hyperdrive: {} Number of crew members: {} \n'.format(self.getRace(),self.getTypeOfCraft(), self.getHyperDrive(), self.getCrew())
        return s
