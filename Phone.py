class Phone:
    def __init__(self, phone_number, phone_type="Personal"):
        self.__phone_number = phone_number
        self.__phone_type = phone_type

    def __str__(self):
        return f"Phone Number: {self.__phone_number} Type: {self.__phone_type}"

    def set_phone_number(self, phone_number):
        self.__phone_number = phone_number

    def set_phone_type(self, phone_type):
        self.__phone_type = phone_type

    def get_phone_number(self):
        return self.__phone_number

    def get_phone_type(self):
        return self.__phone_type