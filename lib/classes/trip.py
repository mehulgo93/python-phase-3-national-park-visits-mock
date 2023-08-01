
class Trip:

    all = []

    def __init__(self, visitor, national_park, start_date, end_date):
        self.visitor = visitor
        self.national_park = national_park
        self.start_date = start_date
        self.end_date = end_date
        Trip.all.append(self)
        pass
    def get_national_park(self):
        return self._national_park
    def set_national_park(self,input):
        from .national_park import NationalPark
        if type(input) == NationalPark:
            self._national_park = input
        else:
            print("Not valid park")
    national_park = property(get_national_park,set_national_park)

    def get_visitor(self):
        return self._visitor
    def set_visitor(self,input):
        from .visitor import Visitor
        if type(input) == Visitor:
            self._visitor = input
        else:
            print("Not valid visitor")
    visitor = property(get_visitor,set_visitor)