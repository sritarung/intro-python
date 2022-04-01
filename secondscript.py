#Sri Tarun Gulumuru
#duration:50 mins
#Question 2

class SchedulerSPM:
    def configure():
        pass
    def __init__(self, data):
        self.data = data
    def __str__(self):												
	return "SchedulerSPM class"
    def Configure(self):												
	pass

class SchedulerAedesAegypti(SchedulerSPM):	
    def __init__(self, data):									
	self.data = data
    def __str__(self):												
	return "SchedulerAedesAegypti class"
    def __Make_Decision__(self):								
	pass
    def __Execute_Decision__(self):							
	pass

class AedesAegypti(SchedulerAedesAegypti):	
    def __init__(self, data):									
	self.data = data
    def __str__(self):												
	return "AedesAegypti class"
    def __life_Stage__(self):										
	pass
    def __energy_Level__(self):									
	pass
    def Birth(self):													
	pass
    def Metamorphosis(self):									
	pass
    def Death(self):													
	pass
    def Flying_Randomly(self):								
	pass
    def Look_For_Resting_Place(self):					
	pass
    def Look_For_Plant(self):									
	pass
    def Feeding(self):												
	pass
    def Mating(self):													
	pass
    def Ovipositing(self):										
	pass

class SchedulerMammal(SchedulerSPM):
    def __init__(self, data):
        self.data=data
    def __str__(self):
        return "SchedulerMammal class"
    def __Execute_Behaviour__(self):
        pass

class Mammal(SchedulerMammal):
    def __init__(self, data):
        self.data=data
    def __str__(self):
        return "Mammal Class"
    def __trace_Intensity__(self):
        pass
    def Moving_Randomly(self):
        pass
    def Update_Trace(self):
        pass

class SchedulerVegetation(SchedulerSPM):
    def __init__(self, data):
        self.data=data
    def __str__(self):
        return "SchedulerVegetation Class"
    def __Update_Trace__(self):
        pass

class Vegetation(SchedulerVegetation):
    def __init__(self, data):
        self.data=data
    def __str__(self):
        return "Vegetation Class"
    def __trace_Intensity__(self):
        pass
    def Update_Trace(self):
        pass

class SchedulerContainer(SchedulerSPM):
    def __init__(self, data):
        self.data=data
    def __str__(self):
        return "SchedulerContainer Class"
    def __Update_Liquid_Level__(self):
        pass
    def __Update_Trace__(self):
        pass
    
class Container(SchedulerContainer):
    def __init__(self,data):
        self.data=data
    def __str__(self):
        return "Container Class"
    def __percentage_Liquid__(self):
        pass
    def __volatility_Liquid__(self):
        pass
    def __percentage_Exposure__(self):
        pass
    def __trace_Intensity__(self):
        pass
    def update_Volume(self):
        pass
    def Update_Trace(self):
        pass

class SchedulerMeteorology(SchedulerSPM):
    def __init__(self, data):
        self.data=data
    def __str__(self):
        return "SchedulerMeteorology Class"
    def __Update_Environment__(self):
        pass

class Meteorology(SchedulerMeteorology):
    def __init__(self, data):
        self.data=data
    def __str__(self):
        return "Meteorology Class"
    def __wind_Direction__(self):
        pass
    def __wind_Direction_Max_Speed__(self):
        pass
    def __accum_Rainfall__(self):
        pass
    def __accum_Solar_Radiation__(self):
        pass
    def __global_Solar_Radiation__(self):
        pass
    def __air_Temp__(self):
        pass
    def __high_Air_Temp__(self):
        pass
    def __low__Air_Temp__(self):
        pass
    def __air_Relative_Humidity__(self):
        pass
    def __wind_Speed__(self):
        pass
    def __high_Wind_Speed__(self):
        pass
    def update_Data(self):
        pass
        
