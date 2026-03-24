class MailingAddress:
    def __init__(self,street,city,state,zipcode=0,type="Unspecified"):
        self.__street = street #string
        self.__city = city #string
        self.__state = state #string
        self.__zipcode = zipcode #int
        self.__type = type #string

    def __str__(self):
        #IDEA: Add strings per line using += and \n
        s = f"Mailing address: {self.__street} {self.__city}, {self.__state}\n"
        s += f"Type: {self.__type}\n"
        s += f"Zipcode: {self.__zipcode}"
        return s #return the fully formed string

    def set_street(self,street):
        self.__street = street
    def set_city(self,city):
        self.__city = city
    def set_state(self,state):
        self.__state = state
    def set_zipcode(self,zipcode):
        self.__zipcode = zipcode
    def set_type(self,type):
        self.__type = type

    def get_street(self):
        return self.__street
    def get_city(self):
        return self.__city
    def get_state(self):
        return self.__state
    def get_zipcode(self):
        return self.__zipcode
    def get_type(self):
        return self.__type