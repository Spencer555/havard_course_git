class Point():
    
    def __init__(self, x, y):
        # storing the data within self
        self.x = x 
        self.y  = y 
        
        
        
p = Point(2, 4)


print(p.x)
print(p.y)


# airline 

class Flight():
    
    def __init__(self, capacity):
        self.capacity = capacity
        self.passengers = []
        
        
    def add_passenger(self, name):
        if self.open_seats():
            self.passengers.append(name) 
            return True
        print("plane is fully booked")
        return False
        
    def open_seats(self):
        return self.capacity - len(self.passengers)
        
            
        
        
        
flight = Flight(3)

names = ["Harry", "Ron", "Hermione", "Ginny"]

for person in names:
    
    if flight.add_passenger(person):
        print(f"Added {person} to flight successfully")
    else:
        print(f"No available seats for {person}")