class Email:
    def __init__(self,email_address,email_type):
        self.__email_address = email_address
        self.__email_type = email_type

    def __str__(self):
        return f"Email address: {self.__email_address} Type: {self.__email_type}"

    def set_email_address(self,email_address): #Setters
        self.__email_address = email_address
    def set_email_type(self,email_type):
        self.__email_type = email_type

    def get_email_address(self): #getters
        return self.__email_address
    def get_email_type(self):
        return self.__email_type