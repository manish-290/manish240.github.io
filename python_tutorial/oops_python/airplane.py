
#python program to cehck the capacity of the plane if it is
#packed or not

class Flight:
    def __init__(self,capacity):
        self.capacity = capacity
        self.passengers= []

    #lets create a function to add the passengers to the flight
    def addPassenger(self,name):
        if not self.open_seat():
            return False
        self.passengers.append(name)
        # self.passengers.append(ticket_no)
        # self.passengers.append(age)
        return True

    #check for the open seats on the plane
    def open_seat(self):
        return self.capacity - len(self.passengers)

flight = Flight(3)

#lets create the list of the passengers  for the flight
people = ["Kiara","Manish","Krishna","Sagar"]
for person in people:
    success = flight.addPassenger(person)
    if success:
        print(f"Added {person}  to flight successfully")
    else:
        print(f"No available seats for {person}")
# print(flight.capacity)

        