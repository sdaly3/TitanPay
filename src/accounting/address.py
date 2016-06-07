class Address:

    def __init__(self, street_address, city, state, zip):
        self.__street_address = street_address
        self.__city = city
        self.__state = state
        self.__zip = zip

    def get_full_address(self):
        return self.__street_address + " " + self.__city + ", " + self.__state + " " + self.__zip
