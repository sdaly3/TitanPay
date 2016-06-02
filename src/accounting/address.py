class Address:
    def __init__(self):
        self.__street_address = "6006 5th Ave N"
        self.__city = "St. Petersburg"
        self.__state = "FL"
        self.__zip = "33712"

    def set_street_address(self, val):
        self.__street_address = val

    def set_city(self, val):
        self.__city = val

    def set_state(self, val):
        self.__state = val

    def set_zip(self, val):
        self.__zip = val

    def get_address(self):
        return self.__street_address

    def get_city(self):
        return self.__city

    def get_state(self):
        return self.__state

    def get_zip(self):
        return self.__zip

if __name__ == "__main__":
        address = Address()
        city = Address()
        state = Address()
        zip = Address()
        print(address.get_address(), city.get_city(), ',', state.get_state(), zip.get_zip())