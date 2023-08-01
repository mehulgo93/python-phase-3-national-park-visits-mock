from .trip import Trip

# national_park.py

# national_park.py

class NationalPark:
    def __init__(self,name):
        if type(name) is str:
            self._name = name
    def get_name(self):
        return self._name
    def set_name(self,newname):
        print("Cannot change")
    name = property(get_name,set_name)

    def trips(self):
        from .trip import Trip
        triplist = []
        for trip in Trip.all:
            if trip.national_park == self:
                triplist.append(trip)
        return triplist

    def visitors(self):
        from .trip import Trip
        vislist = []
        for trip in Trip.all:
            if trip.national_park == self:
                vislist.append(trip.visitor)
        return list(set(vislist))
    
    def total_visits(self):
        from .trip import Trip
        count = 0
        for trip in Trip.all:
            if trip.national_park == self:
                count += 1
        return count
    
    def best_visitor(self):
        from .trip import Trip
        countobject = {}
        for trip in Trip.all:
            if trip.national_park == self:
                if trip.visitor not in countobject:
                    countobject[trip.visitor] = 1
                else:
                    countobject[trip.visitor] += 1
        max_key = max(countobject, key = countobject.get)
        return max_key
        