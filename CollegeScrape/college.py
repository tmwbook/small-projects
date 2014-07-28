__author__ = 'thomas'


class College(object):

    def __init__(self, name, source):
        self.name = name
        self.source = source
        self.public = None
        self.for_profit = None
        self.loc = ''
        self.phone_nmbr = ''


class PhoneNumber(object):

    def __init__(self, area_code, second_half, country_code=1):
        self.country_code = country_code  # int
        self.area_code = area_code  # string
        self.second_half = second_half  # string
        pass

    def to_tuple(self):
        return self.country_code, self.area_code, self.second_half

    def string_number(self):
        number = "("+str(self.country_code)+")"+" ("+self.area_code+")"+\
                 self.second_half
        return number