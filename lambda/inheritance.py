class BMW:
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year

class ThreeSeries(BMW):
    def __init__(self,cruisecontroll,make,model,year):
        BMW.__init__(self,make,model,year)
        self.cruisecontroll = cruisecontroll       #--This where new property has been added in child class


class ThreeSeries(BMW):
    def __init__(self,parkingassistEnabled,make,model,year):
        BMW.__init__(self,make,model,year)
        self.parkingassistEnabled = parkingassistEnabled       #--This where new property has been added in child class



threeseries= ThreeSeries(True,"BMW","AIBeeC",2018)
print(threeseries.make)
print(threeseries.model)
print(threeseries.year)
