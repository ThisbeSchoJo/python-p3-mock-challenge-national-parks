class NationalPark:
    
    def __init__(self, name):
        self.name = name
    
    @property
    def get_name(self):
        return self._name
    
    @get_name.setter
    def name(self, name_value):
        if (not hasattr(self, 'name')) and (type(name_value) == str) and (len(name_value) >= 3):
            self._name = name_value

    def trips(self):
        return [trip for trip in Trip.all if trip.national_park is self]

    def visitors(self):
        return list(set([trip.visitor for trip in self.trips()]))
    
    def total_visits(self):
        return len(self.trips())

    def best_visitor(self):
        # returns Visitor instance that has visited the park the most
        # check the visitor in Trip.all
        visitor_list = [trip.visitor for trip in Trip.all if trip.national_park == self]
        if len(visitor_list) == 0:
            return None
        else:
            return max(visitor_list, key= lambda v: len(v.trips()))
class Trip:
    
    all = []

    def __init__(self, visitor, national_park, start_date, end_date):
        self.visitor = visitor
        self.national_park = national_park
        self.start_date = start_date
        self.end_date = end_date
        Trip.all.append(self)

    @property
    def get_start_date(self):
        return self._start_date
    
    @get_start_date.setter
    def start_date(self, start_date_value):

        valid_suffixes = ("st", "nd", "rd", "th")
        valid_months = [
        "January", "February", "March", "April", "May", "June",
        "July", "August", "September", "October", "November", "December"
        ]

        if (type(start_date_value) == str) and (len(start_date_value) >= 7):
            month = start_date_value.split()[0]
            if (month in valid_months) and (start_date_value.endswith(valid_suffixes)):
                self._start_date = start_date_value

    @property
    def get_end_date(self):
        return self._end_date
    
    @get_end_date.setter
    def end_date(self, end_date_value):

        valid_suffixes = ("st", "nd", "rd", "th")
        valid_months = [
        "January", "February", "March", "April", "May", "June",
        "July", "August", "September", "October", "November", "December"
        ]

        if (type(end_date_value) == str) and (len(end_date_value) >= 7):
            month = end_date_value.split()[0]
            if (month in valid_months) and (end_date_value.endswith(valid_suffixes)):
                self._end_date = end_date_value

    @property
    def get_visitor(self):
        return self._visitor
    
    @get_visitor.setter
    def visitor(self, visitor_value):
        if isinstance(visitor_value, Visitor):
            self._visitor = visitor_value

    @property
    def get_national_park(self):
        return self._national_park
    
    @get_national_park.setter
    def national_park(self, national_park_value):
        if isinstance(national_park_value, NationalPark):
            self._national_park = national_park_value

class Visitor:

    def __init__(self, name):
        self.name = name
    
    @property
    def get_name(self):
        return self._name
    
    @get_name.setter
    def name(self, name_value):
        if (type(name_value) == str) and (1 <= len(name_value) <= 15):
            self._name = name_value

    def trips(self):
        return [trip for trip in Trip.all if trip.visitor is self]
    
    def national_parks(self):
        # returns a unique list of all parks that visitor has visited
        return list(set([trip.national_park for trip in self.trips()]))
        
    def total_visits_at_park(self, park):
        return len([trip for trip in self.trips() if trip.national_park == park])