# visitor.py

class Visitor:
    
    def __init__(self,name):
        if type(name) is str:
            if len(name) <= 15 and len(name) > 0:
                self._name = name

    def get_name(self):
        return self._name
    def set_name(self,newname):
        print("Can't change")
    
    name = property(get_name,set_name)

    def trips(self):
        from .trip import Trip
        vislist = []
        for trip in Trip.all:
            if trip.visitor == self:
                vislist.append(trip)
        return vislist
    def nationalparks(self):
        from .trip import Trip
        parklist = []
        for trip in Trip.all:
            if trip.visitor == self:
                parklist.append(trip.national_park)
        return list(set(parklist))
        
    def create_trip(self, national_park, start_date, end_date):
        from .trip import Trip
        return Trip(self,national_park,start_date,end_date)