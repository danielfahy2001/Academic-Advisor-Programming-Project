class Date:
    def __init__(self,year,month,day):
        self.__year = year
        self.__month = month
        self.__day = day

    def set_year(self,year):
        self.__year = year
    def set_month(self,month):
        self.__month = month
    def set_day(self,day):
        self.__day = day
    def get_year(self):
        return self.__year
    def get_month(self):
        return self.__month
    def get_day(self):
        return self.__day

    #A simple way to display the date.
    def __str__(self):
        return f"{self.__month}/{self.__day}/{self.__year}"